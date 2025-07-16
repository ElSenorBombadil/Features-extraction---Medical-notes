def evaluate_extraction(df_true, df_pred):
    assert len(df_true) == len(
        df_pred), "DataFrames must have the same number of rows"

    # Normalize for comparison: strip, lower, and handle None
    def normalize(val):
        return val.strip().lower() if isinstance(val, str) else ""

    results = {
        "doctor_match": [],
        "patient_match": [],
        "disease_match": [],
        "negated_match": [],
        "drug_match": [],
        "severity_match": [],
        "acuteness_match": []
    }

    for i in range(len(df_true)):
        t = df_true.iloc[i]
        p = df_pred.iloc[i]

        results["doctor_match"].append(
            normalize(t["doctor_name"]) == normalize(p["doctor_name"]))
        results["patient_match"].append(
            normalize(t["patient_name"]) == normalize(p["patient_name"]))
        results["disease_match"].append(
            normalize(t["disease"]) == normalize(p["disease"]))
        results["negated_match"].append(
            normalize(t["negated"]) == normalize(p["negated"]))
        results["drug_match"].append(
            normalize(t["drug"]) == normalize(p["drug"]))
        results["severity_match"].append(
            normalize(t["severity"]) == normalize(p["severity"]))
        results["acuteness_match"].append(
            normalize(t["acuteness"]) == normalize(p["acuteness"]))

    # Convert to binary arrays
    doctor_correct = [int(x) for x in results["doctor_match"]]
    patient_correct = [int(x) for x in results["patient_match"]]
    disease_correct = [int(x) for x in results["disease_match"]]
    negated_correct = [int(x) for x in results["negated_match"]]
    drug_correct = [int(x) for x in results["drug_match"]]
    severity_correct = [int(x) for x in results["severity_match"]]
    acuteness_correct = [int(x) for x in results["acuteness_match"]]

    total_correct = [d & p & pa & n & dr & s & a for d, p, pa, n, dr, s, a in zip(doctor_correct, patient_correct, disease_correct, negated_correct,
                                                                                  drug_correct, severity_correct, acuteness_correct)]

    print("=== Evaluation Results ===")
    print(
        f"Overall Accuracy:       {sum(total_correct) / len(total_correct):.2f}")
    print(
        f"Doctor Accuracy:        {sum(doctor_correct) / len(doctor_correct):.2f}")
    print(
        f"Patient Accuracy:       {sum(patient_correct) / len(patient_correct):.2f}")
    print(
        f"Pathology Accuracy:     {sum(disease_correct) / len(disease_correct):.2f}")
    print(
        f"Negation Accuracy:      {sum(negated_correct) / len(negated_correct):.2f}")
    print(
        f"Drug Accuracy:          {sum(drug_correct) / len(drug_correct):.2f}")
    print(
        f"Severity Accuracy:      {sum(severity_correct) / len(severity_correct):.2f}")
    print(
        f"Acuteness Accuracy:     {sum(acuteness_correct) / len(acuteness_correct):.2f}")
