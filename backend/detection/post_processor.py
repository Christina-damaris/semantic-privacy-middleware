"""
Post Processing for detected entities.

Responsibilities:
1. Remove duplicates.
2. Resolve overlapping detections.
3. Keep highest priority entities.
4. Filter unwanted Presidio detections.
"""

ENTITY_PRIORITY = {

    # Highest priority
    "AWS_ACCESS_KEY":100,
    "AWS_SECRET_KEY":100,
    "RSA_KEY":100,
    "SSH_KEY":100,
    "PRIVATE_KEY_FILE":100,
    "JWT":100,
    "API_KEY":100,
    "BEARER_TOKEN":100,

    "AADHAAR":95,
    "PAN":95,
    "PASSPORT":95,
    "GSTIN":95,
    "SSN":95,

    "BANK_ACCOUNT_NUMBER":90,
    "IFSC":90,
    "IBAN":90,
    "SWIFT":90,

    "EMAIL_ADDRESS":80,
    "PHONE_NUMBER":80,
    "IP_ADDRESS":80,
    "UPI_ID":75,

    "PERSON":60,

    "OTP":30,
    "PIN":30,
    "CVV":30,

    "URL":10,
    "DATE_TIME":10,
    "UK_NHS":10,
}
IGNORE_ENTITIES = {

    "UK_NHS",

    "URL",

    "DATE_TIME"

}
# ============================================================
# Minimum confidence required for certain entities
# ============================================================

MIN_CONFIDENCE = {

    "BANK_ACCOUNT_NUMBER": 0.50,

    "CVV": 0.60,

    "PIN": 0.60,

    "OTP": 0.60,

    "EXPIRY_DATE": 0.60,

    "UPI_ID": 0.85
}
def remove_duplicates(results):
    """
    Removes exact duplicate detections.
    """

    seen = set()

    filtered = []

    for result in results:

        key = (
            result.entity_type,
            result.start,
            result.end
        )

        if key not in seen:

            filtered.append(result)

            seen.add(key)

    return filtered
def remove_ignored(results):

    return [

        r

        for r in results

        if r.entity_type not in IGNORE_ENTITIES

    ]
def filter_low_confidence(results):
    """
    Removes detections whose confidence score
    is below the configured threshold.
    """

    filtered = []

    for result in results:

        threshold = MIN_CONFIDENCE.get(
            result.entity_type,
            0.0
        )

        if result.score >= threshold:

            filtered.append(result)

    return filtered
def get_priority(entity):

    return ENTITY_PRIORITY.get(entity,50)
def resolve_overlaps(results):
    """
    Keeps the higher-priority entity when two detections overlap.
    """

    if not results:
        return []

    # Sort by position, then by descending priority
    results = sorted(
        results,
        key=lambda r: (r.start, -get_priority(r.entity_type))
    )

    filtered = []

    for result in results:

        keep = True

        for existing in filtered:

            overlap = (
                result.start < existing.end
                and
                result.end > existing.start
            )

            if overlap:

                if get_priority(result.entity_type) > get_priority(existing.entity_type):

                    filtered.remove(existing)

                    filtered.append(result)

                keep = False

                break

        if keep:

            filtered.append(result)

    return sorted(filtered,key=lambda r:r.start)
def clean_results(results):
    """
    Complete post-processing pipeline.
    """

    results = remove_duplicates(results)

    results = remove_ignored(results)

    results = filter_low_confidence(results)

    results = resolve_overlaps(results)

    return results