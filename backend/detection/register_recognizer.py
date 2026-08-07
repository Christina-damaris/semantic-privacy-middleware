from presidio_analyzer import RecognizerRegistry
from backend.detection.recognizers.government_ids import government_id_recognizers
from backend.detection.recognizers.financial import financial_recognizers
from backend.detection.recognizers.authentication import authentication_recognizers
from backend.detection.recognizers.cloud_credentials import cloud_credentials_recognizers
from backend.detection.recognizers.crypto_keys import crypto_key_recognizers
from backend.detection.recognizers.health import health_recognizers
from backend.detection.recognizers.health_regex import health_regex_recognizers

def get_registry():
    """
    Returns a Presidio registry containing both
    built-in recognizers and our custom recognizers.
    """

    registry = RecognizerRegistry()

    # Load Presidio recognizers
    registry.load_predefined_recognizers()

    # Government IDs
    for recognizer in government_id_recognizers:
        registry.add_recognizer(recognizer)

    # Financial
    for recognizer in financial_recognizers:
        registry.add_recognizer(recognizer)

    # Authentication
    for recognizer in authentication_recognizers:
        registry.add_recognizer(recognizer)

    # Cloud
    for recognizer in cloud_credentials_recognizers:
        registry.add_recognizer(recognizer)

    # Crypto
    for recognizer in crypto_key_recognizers:
        registry.add_recognizer(recognizer)

    for recognizer in health_recognizers:
        registry.add_recognizer(recognizer)

    for recognizer in health_regex_recognizers:
        registry.add_recognizer(recognizer)    

    return registry