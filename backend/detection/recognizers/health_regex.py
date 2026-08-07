from presidio_analyzer import PatternRecognizer, Pattern

# ==========================================================
# PATIENT ID
# ==========================================================

patient_id_recognizer = PatternRecognizer(

    supported_entity="PATIENT_ID",

    patterns=[

        Pattern(
            name="patient_id",
            regex=r"\b(?:PID|PAT|MRN|UHID)[- ]?\d{4,12}\b",
            score=0.95,
        )

    ]
)

# ==========================================================
# INSURANCE CLAIM ID
# ==========================================================

claim_id_recognizer = PatternRecognizer(

    supported_entity="CLAIM_ID",

    patterns=[

        Pattern(
            name="claim_id",
            regex=r"\b(?:CLM|CLAIM|INS)[- ]?\d{4,15}\b",
            score=0.95,
        )

    ]
)

# ==========================================================
# POLICY NUMBER
# ==========================================================

policy_number_recognizer = PatternRecognizer(

    supported_entity="POLICY_NUMBER",

    patterns=[

        Pattern(
            name="policy_number",
            regex=r"\b(?:POL|POLICY)[- ]?\d{4,15}\b",
            score=0.90,
        )

    ]
)

# ==========================================================
# EXPORT
# ==========================================================

health_regex_recognizers = [

    patient_id_recognizer,

    claim_id_recognizer,

    policy_number_recognizer,
]