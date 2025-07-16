import spacy
import en_ner_bc5cdr_md
# from scispacy.abbreviation import AbbreviationDetector


class SpaCyExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, text):
        doc = self.nlp(text)

        doctor_titles = ["Dr.", "Pr.", "PI", "P.I",
                         "Principal Investigator", "Nurse", "Nurse Practitioner"]
        patient_titles = ["Miss", "Ms.", "Mrs.", "Mr."]
        doctor_name = None
        patient_name = None

        def extract_name(doc, i):
            name = ""
            if i + 1 < len(doc):
                name = doc[i + 1].text
                if i + 2 < len(doc) and doc[i + 2].is_title:
                    name += f" {doc[i + 2].text}"
            return name

        for i, token in enumerate(doc):
            if token.text in doctor_titles and not doctor_name:
                doctor_name = extract_name(doc, i)
            if token.text in patient_titles and not patient_name:
                patient_name = extract_name(doc, i)

        negated = any(tok.dep_ == "neg" for tok in doc)

        severity = "not documented"
        acuteness = "not documented"
        for token in doc:
            word = token.text.lower()
            if word in ["mild", "slight"]:
                severity = "mild"
            elif word == "moderate":
                severity = "moderate"
            elif word in ["severe", "critical", "advanced"]:
                severity = "severe"

            if word in ["acute", "sudden", "rapid"]:
                acuteness = "acute"
            elif word in ["chronic", "persistent", "long-standing"]:
                acuteness = "chronic"

        return {
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "negated": negated,
            "severity": severity,
            "acuteness": acuteness,
            "disease": None,
            "drug": None
        }


class SciSpaCyExtractor:
    def __init__(self):
        self.nlp = en_ner_bc5cdr_md.load()
        self.nlp.add_pipe("abbreviation_detector")

    def extract(self, text):
        doc = self.nlp(text)
        disease = None
        drug = None

        for ent in doc.ents:
            if ent.label_ == "DISEASE" and not disease:
                disease = ent.text
            elif ent.label_ == "CHEMICAL" and not drug:
                drug = ent.text

        return {
            "doctor_name": None,
            "patient_name": None,
            "negated": False,
            "severity": "not documented",
            "acuteness": "not documented",
            "disease": disease,
            "drug": drug
        }
