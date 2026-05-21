
# Local Data Anonymizer

## Author

Enes Gezici  
s34538

A small CLI tool for anonymizing sensitive text in `.json`, `.txt`, `.md`, and `.csv` files using deterministic replacement rules loaded from JSON.

## Requirements

- Python 3.10+

## Installation

```bash
git clone <your-repository-url>
cd s34538_anonymize
```

## Run

### Markdown example

```bash
python anonymize.py --mapping examples/mapping.json --input examples/sample.md --output examples/output/sample.anon.md
```

### CSV example

```bash
python anonymize.py --mapping examples/mapping.json --input examples/sample.csv --output examples/output/sample.anon.csv
```

### JSON example

```bash
python anonymize.py --mapping examples/mapping.json --input examples/sample.json --output examples/output/sample.anon.json
```

## Dry Run

```bash
python anonymize.py --mapping examples/mapping.json --input examples/sample.txt --output examples/output/sample.anon.txt --dry-run
```

## Supported Extensions

- .json
- .txt
- .md
- .csv

## Mapping Format

```json
{
  "replacements": [
    {
      "find": ["Anna Nowak", "A. Nowak"],
      "replace": "PERSON_A"
    },
    {
      "find": ["anna@firma.test"],
      "replace": "EMAIL_A"
    }
  ],
  "options": {
    "case_sensitive": false
  }
}
```

## Overlap Policy

Rules are processed:

1. In the order listed in `replacements`
2. In the order listed inside each `find` array
3. Left-to-right through the text

Earlier replacements can affect later matches.

## Example

Before:

```text
Kontakt: A. Nowak <anna@firma.test>
```

After:

```text
Kontakt: PERSON_A <EMAIL_A>
```
