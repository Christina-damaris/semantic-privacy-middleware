from backend.detection.keyword_loader import load_keywords
from backend.detection.keyword_recognizer import create_keyword_recognizer

# ==========================================================
# HEALTH KEYWORD/DICTIONARY CONFIGURATION
# ==========================================================

HEALTH_FILES = {

    # Dictionary based
    "DIAGNOSIS": ("dictionary", "diagnosis.txt"),
    "MEDICINE": ("dictionary", "medicine.txt"),

    # Keyword based
    "DOCTOR": ("keyword", "doctor.txt"),
    "HOSPITAL": ("keyword", "hospital.txt"),
    "PRESCRIPTION": ("keyword", "prescription.txt"),
    "MEDICAL_REPORT": ("keyword", "medical_report.txt"),
    "LAB_REPORT": ("keyword", "lab_report.txt"),
    "MRI": ("keyword", "mri.txt"),
    "XRAY": ("keyword", "xray.txt"),
    "INSURANCE": ("keyword", "insurance.txt"),
}

health_recognizers = []

for entity_name, (folder, filename) in HEALTH_FILES.items():

    keywords = load_keywords(
        category="health",
        folder=folder,
        filename=filename
    )

    recognizer = create_keyword_recognizer(
        entity_name=entity_name,
        keywords=keywords,
        score=0.85
    )

    health_recognizers.append(recognizer)