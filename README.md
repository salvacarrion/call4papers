# Call4Papers

Get a CSV with topic-related conferences along with their CORE rank, GGS Class, deadlines and more.


## Requirements

- Python +3.6


## Installation

```
git clone git@github.com:salvacarrion/call4papers.git
cd call4papers/
pip install -e .
```


## Usage

**Pre-defined setups: NLP**

```
# Setup with default options for NLP conferences
call4papers --setup "nlp"
```

**Custom keywords, blacklist and ratings:**

```
call4papers --keywords "linguistics, translation, learning" --blacklist "AAAA,BBBB" --ratings "A*,A,B"
```

                                                                                              
**Adding more base setups:**                                                                  
                                                                                              
You can simply edit the file ``call4papers/constants.py`` to add all the setups that you want.


**More options:**

```
usage: call4papers [-h] [--setup {nlp}] [--output_file OUTPUT_FILE] [--keywords KEYWORDS] [--blacklist BLACKLIST] [--ratings RATINGS] [--force_download]
                   [--only_next_year] [--ignore_wikicfp] [--ignore_ggs] [--show-extra]

optional arguments:
  -h, --help            show this help message and exit
  --setup {nlp}         Collection of default setups
  --output_file OUTPUT_FILE
                        Output file
  --keywords KEYWORDS   List of words. Comma-separated.
  --blacklist BLACKLIST
                        List of words (conf. acronyms). Comma-separated.
  --ratings RATINGS     List of words (A*,A,B,C,...). Comma-separated.
  --force_download      Force download, ignoring cache files.
  --only_next_year      Get information only about next year.
  --ignore_wikicfp      Ignore information from Wikicfp.
  --ignore_ggs          Ignore information from GII-GRIN-SCIE (GGS) Conference Rating.
  --show-extra          Show extra columns
```



