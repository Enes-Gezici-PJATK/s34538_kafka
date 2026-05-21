
#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path


SUPPORTED_EXTENSIONS = {".json", ".txt", ".md", ".csv"}


class MappingValidationError(Exception):
    pass


def load_mapping(mapping_path: Path):
    try:
        with mapping_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise MappingValidationError(f"Mapping file not found: {mapping_path}")
    except json.JSONDecodeError as error:
        raise MappingValidationError(f"Invalid JSON in mapping file: {error}")

    if "replacements" not in data:
        raise MappingValidationError("Missing 'replacements' field in mapping file")

    replacements = data["replacements"]

    if not isinstance(replacements, list):
        raise MappingValidationError("'replacements' must be a list")

    validated_rules = []

    for index, rule in enumerate(replacements, start=1):
        if not isinstance(rule, dict):
            raise MappingValidationError(f"Rule #{index} must be an object")

        find_values = rule.get("find")
        replace_value = rule.get("replace")

        if not isinstance(find_values, list):
            raise MappingValidationError(
                f"Rule #{index}: 'find' must be a list"
            )

        if len(find_values) == 0:
            raise MappingValidationError(
                f"Rule #{index}: 'find' list cannot be empty"
            )

        cleaned_find_values = []

        for value in find_values:
            if not isinstance(value, str):
                raise MappingValidationError(
                    f"Rule #{index}: all 'find' entries must be strings"
                )

            if value == "":
                raise MappingValidationError(
                    f"Rule #{index}: empty strings are not allowed in 'find'"
                )

            cleaned_find_values.append(value)

        if not isinstance(replace_value, str):
            raise MappingValidationError(
                f"Rule #{index}: missing or invalid 'replace' value"
            )

        validated_rules.append(
            {
                "find": cleaned_find_values,
                "replace": replace_value,
            }
        )

    options = data.get("options", {})

    if not isinstance(options, dict):
        raise MappingValidationError("'options' must be an object")

    case_sensitive = options.get("case_sensitive", False)

    if not isinstance(case_sensitive, bool):
        raise MappingValidationError(
            "'options.case_sensitive' must be true or false"
        )

    return {
        "replacements": validated_rules,
        "case_sensitive": case_sensitive,
    }


def replace_case_insensitive(text, search, replacement):
    lower_text = text.lower()
    lower_search = search.lower()

    result = []
    index = 0
    replacements_count = 0

    while index < len(text):
        found_at = lower_text.find(lower_search, index)

        if found_at == -1:
            result.append(text[index:])
            break

        result.append(text[index:found_at])
        result.append(replacement)

        index = found_at + len(search)
        replacements_count += 1

    return "".join(result), replacements_count


def apply_replacements(content, rules, case_sensitive=False):
    total_replacements = []

    for rule in rules:
        replace_token = rule["replace"]

        for find_value in rule["find"]:
            if case_sensitive:
                occurrences = content.count(find_value)
                content = content.replace(find_value, replace_token)
            else:
                content, occurrences = replace_case_insensitive(
                    content,
                    find_value,
                    replace_token,
                )

            total_replacements.append(
                {
                    "find": find_value,
                    "replace": replace_token,
                    "count": occurrences,
                }
            )

    return content, total_replacements


def validate_input_file(input_path: Path):
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            "Unsupported file extension. "
            f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )


def read_utf8_file(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise ValueError(f"Invalid UTF-8 encoding in file: {path}")


def write_utf8_file(path: Path, content: str):
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(content, encoding="utf-8")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Local batch anonymizer for JSON/TXT/MD/CSV files"
    )

    parser.add_argument(
        "--mapping",
        required=True,
        help="Path to mapping JSON file",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input file",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to anonymized output file",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show replacement counts without writing output",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    mapping_path = Path(args.mapping)
    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        validate_input_file(input_path)

        mapping = load_mapping(mapping_path)

        content = read_utf8_file(input_path)

        anonymized_content, stats = apply_replacements(
            content,
            mapping["replacements"],
            mapping["case_sensitive"],
        )

        print("Replacement summary:")

        total = 0

        for entry in stats:
            print(
                f"  '{entry['find']}' -> '{entry['replace']}' "
                f"({entry['count']} replacements)"
            )
            total += entry["count"]

        print(f"Total replacements: {total}")

        if args.dry_run:
            print("Dry run enabled. No file written.")
            return

        if input_path.resolve() == output_path.resolve():
            print(
                "Warning: input and output paths are the same. "
                "Original file will be overwritten."
            )

        write_utf8_file(output_path, anonymized_content)

        print(f"Anonymized file written to: {output_path}")

    except (
        MappingValidationError,
        FileNotFoundError,
        ValueError,
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
