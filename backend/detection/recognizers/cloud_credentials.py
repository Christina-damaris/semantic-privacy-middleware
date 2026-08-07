
from presidio_analyzer import PatternRecognizer, Pattern

# ============================================================
# CLOUD CREDENTIAL RECOGNIZERS
# ============================================================

# ------------------------------------------------------------
# AWS ACCESS KEY
# Example:
# AKIAIOSFODNN7EXAMPLE
# ------------------------------------------------------------
aws_access_key_recognizer = PatternRecognizer(
    supported_entity="AWS_ACCESS_KEY",
    patterns=[
        Pattern(
            name="aws_access_key_pattern",
            regex=r"\b(AKIA|ASIA)[A-Z0-9]{16}\b",
            score=0.95,
        )
    ],
    context=[
        "aws",
        "access key",
        "aws access key",
        "access_key_id"
    ]
)

# ------------------------------------------------------------
# AWS SECRET KEY
# Example:
# wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# ------------------------------------------------------------
aws_secret_key_recognizer = PatternRecognizer(
    supported_entity="AWS_SECRET_KEY",
    patterns=[
        Pattern(
            name="aws_secret_key_pattern",
            regex=r"\b[A-Za-z0-9/+=]{40}\b",
            score=0.65,
        )
    ],
    context=[
        "aws secret",
        "secret key",
        "secret_access_key",
        "aws_secret_access_key"
    ]
)

# ------------------------------------------------------------
# AZURE KEY
# Generic Azure API / Subscription Key
# ------------------------------------------------------------
azure_key_recognizer = PatternRecognizer(
    supported_entity="AZURE_KEY",
    patterns=[
        Pattern(
            name="azure_key_pattern",
            regex=r"\b[a-fA-F0-9]{32}\b",
            score=0.55,
        )
    ],
    context=[
        "azure",
        "subscription key",
        "azure key",
        "azure api key"
    ]
)

# ------------------------------------------------------------
# GCP SERVICE ACCOUNT KEY
# Usually referenced inside JSON files
# ------------------------------------------------------------
gcp_service_account_key_recognizer = PatternRecognizer(
    supported_entity="GCP_SERVICE_ACCOUNT_KEY",
    patterns=[
        Pattern(
            name="gcp_private_key_pattern",
            regex=r"-----BEGIN PRIVATE KEY-----[\s\S]*?-----END PRIVATE KEY-----",
            score=0.95,
        )
    ],
    context=[
        "gcp",
        "service account",
        "google cloud",
        "private_key"
    ]
)

# ============================================================
# EXPORT ALL RECOGNIZERS
# ============================================================

cloud_credentials_recognizers = [
    aws_access_key_recognizer,
    aws_secret_key_recognizer,
    azure_key_recognizer,
    gcp_service_account_key_recognizer,
]
