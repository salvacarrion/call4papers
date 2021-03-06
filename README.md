# Call4Papers

Get a CSV with topic-related conferences along with their CORE rank, GGS Class, deadlines, acceptance rates and more. See [csv example](/examples/conferences.csv).

## Requirements

- Python +3.6


## Installation

```
git clone git@github.com:salvacarrion/call4papers.git
cd call4papers/
pip install -e .
```


## Usage

**Pre-defined setups:** NLP or Vision

```
# Setup with default options for NLP conferences
call4papers --setup "nlp"
```

**Custom keywords, blacklist and ratings:**

```
call4papers --keywords "linguistics, translation, learning" --nokeywords "compilers" --blacklist "AAAA,BBBB" --ratings "A*,A,B,1,2"
```

                                                                                              
**Adding more base setups:**                                                                  
                                                                                              
You can simply edit the file ``call4papers/constants.py`` to add all the setups that you want.


**More options:**

```
=> call4papers --help
usage: call4papers [-h] [--setup {nlp,vision,custom,all}] [--output-file OUTPUT_FILE] [--keywords KEYWORDS] [--nokeywords NOKEYWORDS] [--whitelist WHITELIST]
                   [--blacklist BLACKLIST] [--ratings RATINGS] [--force-download] [--show-extra] [--ref-source {core,ggs,all}] [--in-time]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  --setup {nlp,vision,custom,all}
                        Collection of default setups
  --output-file OUTPUT_FILE
                        Output file
  --keywords KEYWORDS   List of words to look for. Comma-separated.
  --nokeywords NOKEYWORDS
                        List of words to exclude. Comma-separated.
  --whitelist WHITELIST
                        List of words (conf. acronyms). Comma-separated.
  --blacklist BLACKLIST
                        List of words (conf. acronyms). Comma-separated.
  --ratings RATINGS     List of words (A*,A,B,C,...). Comma-separated.
  --force-download      Force download, ignoring cache files.
  --show-extra          Show extra columns
  --ref-source {core,ggs,all}
                        Reference source for the LEFT JOIN (all=outer join)
  --in-time             Show only conferences where the deadline has not passed
```



