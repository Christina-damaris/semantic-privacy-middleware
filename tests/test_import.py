import spacy
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

print("spaCy imported successfully")
print("Presidio Analyzer imported successfully")
print("Presidio Anonymizer imported successfully")

nlp = spacy.load("en_core_web_sm")
print("spaCy model loaded successfully")

analyzer = AnalyzerEngine()
print("Analyzer created successfully")

anonymizer = AnonymizerEngine()
print("Anonymizer created successfully")