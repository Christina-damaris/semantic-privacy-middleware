from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()

text = """
Hi, I'm Christina Damaris.
My email is christy@gmail.com
My phone number is +91 9876543210.
My Aadhaar number is 1234 5678 9012.
My IP address is 192.168.1.1.
"""

results = analyzer.analyze(
    text=text,
    language="en"
)

print("Detected Entities\n")

for result in results:
    print(
        f"{result.entity_type:<20}"
        f"Score:{result.score:.2f}"
        f" -> {text[result.start:result.end]}"
    )