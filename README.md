# Call4Papers

Get a CSV with topic-related conferences along with their CORE rank, deadlines and more

## Requirements

- Python +3.6

## Installation

```
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