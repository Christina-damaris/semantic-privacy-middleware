from presidio_analyzer import PatternRecognizer, Pattern

# ============================================================
# CRYPTOGRAPHIC KEY RECOGNIZERS
# ============================================================

# ------------------------------------------------------------
# RSA PRIVATE KEY
# ------------------------------------------------------------
rsa_key_recognizer = PatternRecognizer(
    supported_entity="RSA_KEY",
    patterns=[
        Pattern(
            name="rsa_private_key",
            regex=r"-----BEGIN RSA PRIVATE KEY-----[\s\S]*?-----END RSA PRIVATE KEY-----",
            score=0.99,
        )
    ],
    context=[
        "rsa",
        "private key",
        "pem",
        "key"
    ]
)

# ------------------------------------------------------------
# OPENSSH PRIVATE KEY
# ------------------------------------------------------------
ssh_key_recognizer = PatternRecognizer(
    supported_entity="SSH_KEY",
    patterns=[
        Pattern(
            name="openssh_private_key",
            regex=r"-----BEGIN OPENSSH PRIVATE KEY-----[\s\S]*?-----END OPENSSH PRIVATE KEY-----",
            score=0.99,
        )
    ],
    context=[
        "ssh",
        "openssh",
        "private key",
        "authorized_keys"
    ]
)

# ------------------------------------------------------------
# X509 CERTIFICATE
# ------------------------------------------------------------
certificate_recognizer = PatternRecognizer(
    supported_entity="CERTIFICATE",
    patterns=[
        Pattern(
            name="certificate",
            regex=r"-----BEGIN CERTIFICATE-----[\s\S]*?-----END CERTIFICATE-----",
            score=0.99,
        )
    ],
    context=[
        "certificate",
        "ssl",
        "tls",
        "pem",
        "x509"
    ]
)

# ------------------------------------------------------------
# PRIVATE KEY FILE (Generic)
# Detects generic PEM private keys
# ------------------------------------------------------------
private_key_file_recognizer = PatternRecognizer(
    supported_entity="PRIVATE_KEY_FILE",
    patterns=[
        Pattern(
            name="generic_private_key",
            regex=r"-----BEGIN PRIVATE KEY-----[\s\S]*?-----END PRIVATE KEY-----",
            score=0.99,
        )
    ],
    context=[
        "private key",
        "pem",
        "key file"
    ]
)

# ============================================================
# EXPORT ALL RECOGNIZERS
# ============================================================

crypto_key_recognizers = [
    rsa_key_recognizer,
    ssh_key_recognizer,
    certificate_recognizer,
    private_key_file_recognizer,
]