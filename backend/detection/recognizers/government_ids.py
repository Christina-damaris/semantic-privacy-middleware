from presidio_analyzer import PatternRecognizer, Pattern

# Aadhaar
aadhaar_recognizer = PatternRecognizer(
    supported_entity="AADHAAR",
    patterns=[
        Pattern(
            name="aadhaar_pattern",
            regex=r"\b\d{4}\s?\d{4}\s?\d{4}\b",
            score=0.85
        )
    ]
)

# PAN
pan_recognizer = PatternRecognizer(
    supported_entity="PAN",
    patterns=[
        Pattern(
            name="pan_pattern",
            regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
            score=0.90
        )
    ]
)

# Passport (Indian passport format)
passport_recognizer = PatternRecognizer(
    supported_entity="PASSPORT",
    patterns=[
        Pattern(
            name="passport_pattern",
            regex=r"\b[A-Z][0-9]{7}\b",
            score=0.85
        )
    ]
)

# GSTIN
gstin_recognizer = PatternRecognizer(
    supported_entity="GSTIN",
    patterns=[
        Pattern(
            name="gstin_pattern",
            regex=r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b",
            score=0.90
        )
    ]
)

# SSN (US)
ssn_recognizer = PatternRecognizer(
    supported_entity="SSN",
    patterns=[
        Pattern(
            name="ssn_pattern",
            regex=r"\b\d{3}-\d{2}-\d{4}\b",
            score=0.90
        )
    ]
)


government_id_recognizers = [
    aadhaar_recognizer,
    pan_recognizer,
    passport_recognizer,
    gstin_recognizer,
    ssn_recognizer,
]