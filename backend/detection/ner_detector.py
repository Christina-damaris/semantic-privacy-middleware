from presidio_analyzer import AnalyzerEngine
from backend.detection.post_processor import clean_results
from backend.detection.register_recognizer import get_registry
from backend.detection.entity_mapper import get_entity_details

registry = get_registry()

analyzer = AnalyzerEngine(
    registry=registry
)

text = """
Hi, I'm Christina Damaris.

Email:
christy@gmail.com

Phone:
+91 9876543210

Aadhaar:
1234 5678 9012

PAN:
ABCDE1234F

IFSC:
SBIN0001234

JWT:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiY2hyaXN0eSJ9.signature

AWS Access Key:
AKIAIOSFODNN7EXAMPLE

IP:
192.168.1.1
"""

results = analyzer.analyze(
    text=text,
    language="en"
)

results = clean_results(results)
# ---------- PRINT RESULTS ----------

print("\nDetected Entities\n")

for result in results:

    details = get_entity_details(result.entity_type)

    print("--------------------------------")

    print("Entity :", result.entity_type)

    print("Matched:", text[result.start:result.end])

    print("Score  :", round(result.score, 2))

    if details:
        print("Category :", details["category"])
        print("Action   :", details["action"])
        print("Risk     :", details["risk"])
    else:
        print("Category : Unknown")