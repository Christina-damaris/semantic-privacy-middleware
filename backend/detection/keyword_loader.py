from pathlib import Path

# ==========================================================
# Root folder containing all keyword categories
# ==========================================================

KEYWORD_ROOT = Path(__file__).parent / "keywords"


def load_keywords(category: str, folder: str, filename: str):
    """
    Load keywords from a text file.

    Example:
        load_keywords(
            category="health",
            folder="keyword",
            filename="doctor.txt"
        )

        load_keywords(
            category="health",
            folder="dictionary",
            filename="diagnosis.txt"
        )
    """

    file_path = KEYWORD_ROOT / category / folder / filename

    if not file_path.exists():
        print(f"[WARNING] Keyword file not found: {file_path}")
        return []

    keywords = []

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            keyword = line.strip()

            # Ignore blank lines
            if not keyword:
                continue

            # Ignore comments
            if keyword.startswith("#"):
                continue

            keywords.append(keyword.lower())

    # Remove duplicates while preserving order
    keywords = list(dict.fromkeys(keywords))

    return keywords