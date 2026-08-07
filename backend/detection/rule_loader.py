import json
from pathlib import Path


def load_rule_table():
    """
    Loads Hinja's rule table.
    """

    project_root = Path(__file__).resolve().parents[2]

    rule_path = project_root / "risk-engine" / "rule_table.json"

    with open(rule_path, "r", encoding="utf-8") as file:
        return json.load(file)