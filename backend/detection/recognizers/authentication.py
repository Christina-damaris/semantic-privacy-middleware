from presidio_analyzer import PatternRecognizer, Pattern

# ============================================================
# AUTHENTICATION RECOGNIZERS
# ============================================================

# ------------------------------------------------------------
# JWT
# Example:
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
# eyJzdWIiOiIxMjM0NTY3ODkwIn0.
# SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
# ------------------------------------------------------------
jwt_recognizer = PatternRecognizer(
    supported_entity="JWT",
    patterns=[
        Pattern(
            name="jwt_pattern",
            regex=r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b",
            score=0.95,
        )
    ],
    context=[
        "jwt",
        "token",
        "access token",
        "authorization"
    ]
)

# ------------------------------------------------------------
# Bearer Token
# Example:
# Bearer eyJhbGc...
# ------------------------------------------------------------
bearer_token_recognizer = PatternRecognizer(
    supported_entity="BEARER_TOKEN",
    patterns=[
        Pattern(
            name="bearer_pattern",
            regex=r"Bearer\s+[A-Za-z0-9\-._~+/]+=*",
            score=0.90,
        )
    ],
    context=[
        "bearer",
        "authorization",
        "access token"
    ]
)

# ------------------------------------------------------------
# API KEY
# Covers common prefixes
# sk-xxxxxxxx
# pk-xxxxxxxx
# api_xxxxxx
# ------------------------------------------------------------
api_key_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[
        Pattern(
            name="api_key_pattern",
            regex=r"\b(?:sk|pk|rk|api)[-_][A-Za-z0-9_\-]{16,}\b",
            score=0.80,
        )
    ],
    context=[
        "api key",
        "apikey",
        "secret key",
        "token"
    ]
)

# ------------------------------------------------------------
# OTP
# Usually 4–8 digits
# ------------------------------------------------------------
otp_recognizer = PatternRecognizer(
    supported_entity="OTP",
    patterns=[
        Pattern(
            name="otp_pattern",
            regex=r"\b\d{4,8}\b",
            score=0.35,
        )
    ],
    context=[
        "otp",
        "verification code",
        "verification",
        "one time password",
        "authentication code"
    ]
)

# ------------------------------------------------------------
# PIN
# Usually 4–6 digits
# ------------------------------------------------------------
pin_recognizer = PatternRecognizer(
    supported_entity="PIN",
    patterns=[
        Pattern(
            name="pin_pattern",
            regex=r"\b\d{4,6}\b",
            score=0.35,
        )
    ],
    context=[
        "pin",
        "atm pin",
        "security pin",
        "transaction pin"
    ]
)

# ------------------------------------------------------------
# SESSION ID
# Generic session identifiers
# ------------------------------------------------------------
session_id_recognizer = PatternRecognizer(
    supported_entity="SESSION_ID",
    patterns=[
        Pattern(
            name="session_pattern",
            regex=r"\b[a-fA-F0-9]{32,64}\b",
            score=0.45,
        )
    ],
    context=[
        "session",
        "session id",
        "sessionid",
        "cookie"
    ]
)

# ============================================================
# EXPORT ALL RECOGNIZERS
# ============================================================

authentication_recognizers = [
    jwt_recognizer,
    bearer_token_recognizer,
    api_key_recognizer,
    otp_recognizer,
    pin_recognizer,
    session_id_recognizer,
]