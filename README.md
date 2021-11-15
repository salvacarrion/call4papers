# Call4Papers

Get a CSV with topic-related conferences along with their CORE rank, deadlines and more


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


**More ptions:**

```
usage: main.py [-h] [--setup {nlp}] [--output_file OUTPUT_FILE]
               [--keywords KEYWORDS] [--blacklist BLACKLIST]
               [--ratings RATINGS] [--force_download] [--ignore_wikicfp]
               [--only_next_year]

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
  --ignore_wikicfp      Ignore Wikicfp information.
  --only_next_year      Get information only about next year.
```



