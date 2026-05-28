from pathlib import Path
import json


def test_anonymized_output_exists():
    path = Path("integration/pipeline/anonymized.json")
    assert path.exists()


def test_email_was_anonymized():
    path = Path("integration/pipeline/anonymized.json")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    text = json.dumps(data)

    assert "EMAIL_01" in text