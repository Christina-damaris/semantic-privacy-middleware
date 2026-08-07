import re

from presidio_analyzer import PatternRecognizer, Pattern


def create_keyword_recognizer(
    entity_name: str,
    keywords: list,
    score: float = 0.85
):
    """
    Creates a keyword-based Presidio recognizer.
    """

    # Remove empty keywords
    keywords = [k.strip() for k in keywords if k.strip()]

    # If no keywords are available,
    # return an empty recognizer.
    if not keywords:

        return PatternRecognizer(
            supported_entity=entity_name,
            patterns=[]
        )

    # Escape regex special characters
    escaped = [

        re.escape(keyword)

        for keyword in keywords

    ]

    # Case-insensitive regex
    regex = r"(?i)\b(" + "|".join(escaped) + r")\b"

    return PatternRecognizer(

        supported_entity=entity_name,

        patterns=[

            Pattern(

                name=f"{entity_name}_keywords",

                regex=regex,

                score=score

            )

        ]

    )