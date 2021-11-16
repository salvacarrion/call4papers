import os
import argparse
import datetime
import requests
from pathlib import Path

import urllib.parse
from urllib.error import HTTPError

import pandas as pd
from thefuzz import process
from tqdm import tqdm
from bs4 import BeautifulSoup

from call4papers.constants import MINIMAL_COLUMNS, DEFAULT_SETUPS


def get_core_conferences(force_download, cache_dir="."):
    # Get filename
    year = int(datetime.datetime.now().year)
    core_code = f"CORE{year}"
    filename = os.path.join(cache_dir, f"cache_{core_code.lower()}.csv")

    # Get conferences
    if not force_download and os.path.exists(filename):  # Load file
        print(f"Loading from cache... ({os.path.abspath(filename)})")
        df = pd.read_csv(filename)
        print(f"File CORE loaded! ({len(df)} rows)")
    else:
        # Scrape CORE
        print("No cached file. The CORE download is about to start...")
        df = scrape_core_conferences(savepath=filename, core_code=core_code)
        print("CORE scraped!")
    return df


def scrape_core_conferences(savepath, core_code, pages=100):
    # core: 'all', CORE{YEAR}
    tables = []

    # Get COREs
    print("Downloading conferences from 'portal.core.edu.au'...")
    for i in tqdm(range(1, pages), total=pages):
        try:
            url = f"http://portal.core.edu.au/conf-ranks/?search=&by=acronym&source={core_code}&sort=arank&page={i}"
            table_i = pd.read_html(url)
            if table_i:
                tables.append(table_i[0])
        except HTTPError as e:
            if i > 1 and e.code == 500:
                print("No more pages to scrape")
            else:
                print(e)
            break

    # Concat tables
    df = pd.concat(tables)

    # Save table
    df.to_csv(savepath, index=False)
    print(f"Cached file saved! ({os.path.abspath(savepath)})")
    return df


def get_ggs_conferences(force_download, cache_dir="."):
    filename = os.path.join(cache_dir, f"cache_gii-grin-scie.xlsx")

    # Get conferences
    if not force_download and os.path.exists(filename):  # Load file
        print(f"Loading GGS from cache... ({os.path.abspath(filename)})")
        df = pd.read_excel(filename, header=[1])
        print(f"File loaded! ({len(df)} rows)")
    else:
        # Scrape CORE
        print("No cached file. The GGS download is about to start...")
        df = scrape_ggs_conferences(savepath=filename)
        print("GGS scraped!")
    return df


def scrape_ggs_conferences(savepath):
    ggs_url = "https://scie.lcc.uma.es:8443/"

    # Get index
    print("Downloading conferences from 'scie.lcc.uma.es'...")
    response = requests.get(
        url=ggs_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        }
    )

    # Check correctness
    if response.status_code != 200:
        raise ConnectionError("Invalid request for GGS")

    # Get XLXS file
    soup = BeautifulSoup(response.text, 'lxml')
    xlxs_href = soup.select_one("#text > div.entry > table:nth-child(1) > tbody > tr > td:nth-child(2) > a[href]").attrs["href"]
    xlxs_href = urllib.parse.urljoin(ggs_url, xlxs_href)

    # Download file
    response = requests.get(xlxs_href, allow_redirects=True)
    if response.status_code != 200:
        raise ConnectionError("Invalid request for GGS")

    # Save xlsx
    with open(savepath, 'wb') as f:
        f.write(response.content)
    print("File saved!")

    # Open file
    df = pd.read_excel(savepath, header=[1])
    return df


def filter_conferences(df, keywords, blacklist, ratings):
    # Filter by keywords
    if keywords:
        kw_filter = '|'.join(keywords).lower()
        df = df[df['Title'].str.contains(kw_filter, case=False, regex=True)]

    # Filter by blacklist
    if blacklist:
        kw_filter = '|'.join(blacklist).lower()
        df = df[~df['Acronym'].str.contains(kw_filter, case=False, regex=True)]

    # Filter by rating
    if ratings:
        df = df[df['Rank'].apply(lambda x: any(x.strip().upper() == rat.strip().upper() for rat in ratings))]
    return df


def fuzzy_matching(df, title, threshold=0.75):
    if len(df) >= 2:
        ratios = process.extract(title, list(df["When"]))
        best_title, best_score = ratios[0]
        if best_score >= threshold:
            for i, (_, row) in enumerate(df.iterrows()):   # i starts at 1
                if row["When"] == best_title:  # Check title
                    return df[i:i+2], best_score
    return None, 0.0


def get_deadlines(title, acronym, year='f', only_next_year=False):
    # year: all='a', 2021='t', 2021+='f', 2022='n'
    results = []

    # Get table
    url = f"http://www.wikicfp.com/cfp/servlet/tool.search?q={urllib.parse.quote(acronym)}&year={year}"
    tables = pd.read_html(url)

    # Get table with 4 cols
    df = None
    for t_df in tables:
        if len(t_df.shape) == 2 and t_df.shape[1] == 4:
            df = t_df
            break

    # Check if there is any table
    if df is not None:

        # Make first row header
        if set(df.iloc[0]) == {'Deadline', 'Event', 'Where', 'When'}:
            new_header = df.iloc[0]  # grab the first row for the header
            df = df[1:]  # take the data less the header row
            df.columns = new_header  # set the header row as the df header

        # Check if exist exact acronym (this year and next)
        year = int(datetime.datetime.now().year)
        list_years = [year+1] if only_next_year else [year, year+1]
        for yr in list_years:
            df_yr = df.loc[df['Event'] == f"{acronym} {yr}"]

            # 1) Re-Check using fuzzy match
            # 2) If there are more than one, select using fuzzy matching
            df_yr, thrs = fuzzy_matching(df_yr, title)

            # Check output correctness
            if df_yr is not None and len(df_yr) == 2:
                values = {"Event year": int(yr),
                          "when": df_yr.iloc[1]["When"],
                          "where": df_yr.iloc[1]["Where"],
                          "deadline": df_yr.iloc[1]["Deadline"],
                          }
                results.append(values)
            else:
                print(f'No exact match has been found ({thrs}% matching): {acronym} {yr} | {title}')
    return results


def prettify_csv(df, show_extra):
    # Rename columns
    df = df.rename(columns={"Rank": "CORE rank"})

    # Show minimal columns
    if not show_extra:
        columns = [c for c in MINIMAL_COLUMNS if c in set(df.columns)]
        df = df[columns]
    return df


def search4papers(output_file, keywords, blacklist, ratings, ignore_wikicfp, ignore_ggs,
                  only_next_year, force_download, show_extra):
    # Create cache folder if it does not exists
    cache_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".cache"))
    p = Path(cache_dir)
    p.mkdir(parents=True, exist_ok=True)

    # Get CORE conferences
    df_core = get_core_conferences(force_download=force_download, cache_dir=cache_dir)

    # Add GGS information
    if not ignore_ggs:
        # Get GGS conferences
        df_ggs = get_ggs_conferences(force_download=force_download, cache_dir=cache_dir)

        # Rename columns and remove index column
        df_ggs = df_ggs.rename(columns={"Title": "GGS_title", "Acronym": "Acronym"}).drop([0], axis=1)

        # Left join
        df = pd.merge(df_core, df_ggs, on='Acronym', how='left')

    else:  # alias
        df = df_core
    # Filter conferences
    df = filter_conferences(df, keywords=keywords, blacklist=blacklist, ratings=ratings)

    # Add Wikicfp information
    if not ignore_wikicfp:
        new_rows = []
        for i, row in tqdm(df.iterrows(), total=len(df)):
            # if row["Acronym"] != "IEA/AIE":
            #     continue
            results = get_deadlines(title=row["Title"], acronym=row["Acronym"], only_next_year=only_next_year)

            if len(results) == 0:
                d = dict(row)
                new_rows.append(d)
            elif len(results) > 0:
                for r in results:
                    d = dict(list(dict(row).items()) + list(r.items()))
                    new_rows.append(d)

        # Create new Dataframe
        df = pd.DataFrame(new_rows)

        # Force types
        df.astype({"Event year": int}, errors='ignore')

    # Save table
    if output_file:
        # Prettify output
        df = prettify_csv(df, show_extra)

        # Save file
        df.to_csv(output_file, index=False)
        print(f"File saved! ({os.path.abspath(output_file)})")


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--setup', type=str, default=None, choices=list(DEFAULT_SETUPS.keys()),
                        help='Collection of default setups')
    parser.add_argument('--output_file', type=str, default="conferences.csv", help='Output file')
    parser.add_argument('--keywords', type=str, default=None, help='List of words. Comma-separated.')
    parser.add_argument('--blacklist', type=str, default=None, help='List of words (conf. acronyms). Comma-separated.')
    parser.add_argument('--ratings', type=str, default=None, help='List of words (A*,A,B,C,...). Comma-separated.')
    parser.add_argument('--force_download', action='store_true', help='Force download, ignoring cache files.')
    parser.add_argument('--only_next_year', action='store_true', help='Get information only about next year.')
    parser.add_argument('--ignore_wikicfp', action='store_true', help='Ignore information from Wikicfp.')
    parser.add_argument('--ignore_ggs', action='store_true', help='Ignore information from GII-GRIN-SCIE (GGS) Conference Rating.')
    parser.add_argument('--show-extra', action='store_true', help='Show extra columns')

    # Pars vars
    args = parser.parse_args()

    # Default vars
    if args.setup:
        keywords = DEFAULT_SETUPS[args.setup]["keywords"]
        blacklist = DEFAULT_SETUPS[args.setup]["blacklist"]
        ratings = DEFAULT_SETUPS[args.setup]["ratings"]
    else:
        keywords = {} if args.keywords is None else set(args.keywords.split(","))
        blacklist = {} if args.blacklist is None else set(args.blacklist.split(","))
        ratings = {} if args.ratings is None else set(args.ratings.split(","))

    # Run
    search4papers(force_download=args.force_download, output_file=args.output_file,
                  keywords=keywords, blacklist=blacklist, ratings=ratings,
                  ignore_wikicfp=args.ignore_wikicfp, ignore_ggs=args.ignore_ggs,
                  only_next_year=args.only_next_year, show_extra=args.show_extra)


if __name__ == '__main__':
    main()
