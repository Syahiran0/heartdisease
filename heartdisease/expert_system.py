# expert_system.py

def diagnose(inputs):
    heart_rate = inputs.get("heart_rate")
    chest_pain = inputs.get("chest_pain")
    blood_pressure = inputs.get("blood_pressure")
    age = inputs.get("age")
    ecg = inputs.get("ecg")
    cholesterol = inputs.get("cholesterol")
    blood_sugar = inputs.get("blood_sugar")
    breathing = inputs.get("breathing")
    fatigue = inputs.get("fatigue")
    joint_pain = inputs.get("joint_pain")

    # Intermediate conditions
    coronary_blockage = False
    cardiac_block_risk = False
    rheumatic_sign = False
    rheumatic_symptom = False
    weak_heart_indicator = False
    fatigue_index = False

    # Rule 1
    symptom_severity = "low"
    if heart_rate > 100 and chest_pain == "severe":
        symptom_severity = "high"

    # Rule 2
    risk_factor = "low"
    if blood_pressure > 140 and age > 50:
        risk_factor = "high"

    # Rule 3
    cardiac_signal = "low"
    if ecg == "abnormal" and chest_pain == "mild":
        cardiac_signal = "medium"

    # Rule 4
    metabolic_stress = "low"
    if cholesterol > 200 and blood_sugar > 140:
        metabolic_stress = "high"

    # Rule 5
    chest_stress = "low"
    if chest_pain == "painful" and breathing == "short":
        chest_stress = "high"

    # Rule 6
    if heart_rate < 60 and fatigue == "high":
        fatigue_index = True

    # Rule 7
    if ecg == "irregular" and heart_rate > 90:
        cardiac_signal = "high"

    # Rule 8
    if joint_pain == "present" and age > 45:
        rheumatic_sign = True

    # Rule 9
    if cholesterol > 250 and age > 50:
        cardiac_block_risk = True

    # Rule 10
    if ecg == "abnormal" and chest_pain == "severe" and cholesterol > 200:
        coronary_blockage = True

    # Rule 11
    if joint_pain == "severe" and age < 40:
        rheumatic_symptom = True

    # Rule 12
    if fatigue == "high" and heart_rate < 60:
        weak_heart_indicator = True

    # Rule 13
    if coronary_blockage or cardiac_block_risk:
        diagnosis = "Coronary Heart Disease"
    # Rule 14
    elif rheumatic_sign or rheumatic_symptom:
        diagnosis = "Rheumatic Heart Disease"
    # Rule 15
    elif weak_heart_indicator or fatigue_index:
        diagnosis = "Weak Heart Disease"
    else:
        diagnosis = "No significant heart risk detected"

    return diagnosis
