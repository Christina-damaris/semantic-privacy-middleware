from presidio_analyzer import PatternRecognizer, Pattern

# ============================================================
# FINANCIAL INFORMATION RECOGNIZERS
# ============================================================

# # ------------------------------------------------------------
# BANK ACCOUNT NUMBER
# ------------------------------------------------------------
bank_account_recognizer = PatternRecognizer(
    supported_entity="BANK_ACCOUNT_NUMBER",
    patterns=[
        Pattern(
            name="bank_account_pattern",
            regex=r"\b\d{9,18}\b",
            score=0.30,
        )
    ],
    context=[
        "account",
        "account number",
        "account no",
        "bank",
        "a/c",
        "acct",
        "saving account",
        "current account"
    ]
)
# ------------------------------------------------------------
# IFSC CODE (India)
# Example: SBIN0001234
# ------------------------------------------------------------
ifsc_recognizer = PatternRecognizer(
    supported_entity="IFSC",
    patterns=[
        Pattern(
            name="ifsc_pattern",
            regex=r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
            score=0.80,
        )
    ],
    context=[
        "ifsc",
        "bank",
        "branch",
        "bank code"
    ]
)

# ------------------------------------------------------------
# SWIFT / BIC CODE
# Example:
# HDFCINBB
# HDFCINBBXXX
# ------------------------------------------------------------
swift_recognizer = PatternRecognizer(
    supported_entity="SWIFT",
    patterns=[
        Pattern(
            name="swift_pattern",
            regex=r"\b[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?\b",
            score=0.80,
        )
    ],
    context=[
        "swift",
        "bic",
        "swift code",
        "bank transfer"
    ]
)

# ------------------------------------------------------------
# CVV
# Example:
# CVV : 123
# Security Code : 456
# ------------------------------------------------------------
cvv_recognizer = PatternRecognizer(
    supported_entity="CVV",
    patterns=[
        Pattern(
            name="cvv_pattern",
            regex=r"\b\d{3,4}\b",
            score=0.35,
        )
    ],
    context=[
        "cvv",
        "cvc",
        "cvv2",
        "security code",
        "card verification"
    ]
)

# ------------------------------------------------------------
# CARD EXPIRY DATE
# Examples:
# 12/27
# 12-27
# 12/2027
# 12-2027
# ------------------------------------------------------------
expiry_date_recognizer = PatternRecognizer(
    supported_entity="EXPIRY_DATE",
    patterns=[
        Pattern(
            name="expiry_pattern",
            regex=r"\b(0[1-9]|1[0-2])[/-](\d{2}|\d{4})\b",
            score=0.45,
        )
    ],
    context=[
        "expiry",
        "expiration",
        "expires",
        "valid till",
        "valid thru",
        "exp"
    ]
)

# ------------------------------------------------------------
# UPI ID
# Examples:
# christy@ybl
# user123@okaxis
# demo@ibl
# ------------------------------------------------------------
upi_recognizer = PatternRecognizer(
    supported_entity="UPI_ID",
    patterns=[
        Pattern(
            name="upi_pattern",
            regex=r"\b[a-zA-Z0-9._-]+@(ybl|ibl|okaxis|okhdfcbank|oksbi|okicici|paytm|axl)\b",
            score=0.95,
        )
    ],
    context=[
        "upi",
        "upi id",
        "payment",
        "phonepe",
        "gpay",
        "google pay",
        "paytm",
        "bhim"
    ]
)
# ------------------------------------------------------------
# IBAN
# International Bank Account Number
# Example:
# GB82WEST12345698765432
# ------------------------------------------------------------
iban_recognizer = PatternRecognizer(
    supported_entity="IBAN",
    patterns=[
        Pattern(
            name="iban_pattern",
            regex=r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b",
            score=0.80,
        )
    ],
    context=[
        "iban",
        "international bank account",
        "wire transfer"
    ]
)

# ============================================================
# EXPORT ALL RECOGNIZERS
# ============================================================

financial_recognizers = [
    bank_account_recognizer,
    ifsc_recognizer,
    swift_recognizer,
    cvv_recognizer,
    expiry_date_recognizer,
    upi_recognizer,
    iban_recognizer,
]