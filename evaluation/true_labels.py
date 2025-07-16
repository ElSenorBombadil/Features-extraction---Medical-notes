import pandas as pd

# expected columsn after extraction
columns = ["doctor_name", "patient_name", "disease",
           "negated", "drug", "severity", "acuteness"]

# True labels
df_true = pd.DataFrame(data={
    "doctor_name": ["Evans", "L. Meyer", "Angela", None, "John", None, "Leah Davis", "Kamal", "Rose", "Kim", None],
    "patient_name": ["Blake", "Carla Hughes", "Dane", "R. Grant", "Ray", "Tomlinson", "Jennifer", "Zoe Green",
                     "Barret", "A. Lee", "Doe"],
    "disease": ["kidney stones", "diabetes", "high blood pressure", "fatigue",
                "cancer", "heart condition", "asthma", "tuberculosis", "pneumonia", "depression",
                "metastasis"],
    "negated": [False, True, False, False, True, False, False, True, False, False, False],
    "drug": [None, None, "ibuprofen", None, None, None, "antibiotics", None, None, None, None],
    "severity": ["not documented", "not documented", "not documented", "not documented", "not documented",
                 "not documented", "severe", "not documented", "not documented", "not documented",
                 "not documented"],
    "acuteness": ["not documented", "not documented", "not documented", "chronic", "not documented",
                  "not documented", "not documented", "not documented", "not documented", "not documented",
                  "not documented"]
}, columns=columns)
