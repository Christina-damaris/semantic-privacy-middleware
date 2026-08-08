from pathlib import Path

# ==========================================================
# CHANGE THIS TO YOUR ICD FILE LOCATION
# ==========================================================

SOURCE_FILE = Path(
    r"C:\g_downloads\icd10cm-Code Descriptions-2026\icd10cm-codes-2026.txt"
)

# ==========================================================
# Automatically locate the project root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    PROJECT_ROOT
    / "backend"
    / "keywords"
    / "health"
    / "dictionary"
    / "diagnosis.txt"
)
diagnoses = set()

with open(SOURCE_FILE, "r", encoding="utf-8") as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

        parts = line.split(maxsplit=1)

        if len(parts) < 2:
            continue

        description = parts[1].strip()

        diagnoses.add(description.lower())

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

    for diagnosis in sorted(diagnoses):

        file.write(diagnosis + "\n")

print("=" * 60)
print(" ICD-10 Dictionary Generated Successfully")
print("=" * 60)
print(f"Total Diagnoses : {len(diagnoses):,}")
print(f"Saved To        : {OUTPUT_FILE}")
print("=" * 60)