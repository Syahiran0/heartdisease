# expert_system.py

def diagnose(inputs):

    heart_rate = inputs["heart_rate"]
    chest_pain = inputs["chest_pain"]
    blood_pressure = inputs["blood_pressure"]
    age = inputs["age"]
    ecg = inputs["ecg"]
    cholesterol = inputs["cholesterol"]
    breathing = inputs["breathing"]
    fatigue = inputs["fatigue"]
    joint_pain = inputs["joint_pain"]
    fever = inputs["fever"]
    murmur = inputs["murmur"]
    swelling = inputs["swelling"]
    smoking = inputs["smoking"]
    diabetes = inputs["diabetes"]

    # ---------------------------
    # RULES
    # ---------------------------

    # R1 – Coronary Heart Disease
    if (chest_pain == "Severe" and
        ecg == "Abnormal" and
        cholesterol == "High (≥240)"):
        return "Coronary Heart Disease"

    # R2 – Coronary Heart Disease
    if (age > 60 and
        blood_pressure == "High" and
        100 < heart_rate < 121):
        return "Coronary Heart Disease"

    # R3 – Coronary Heart Disease
    if (smoking == "Smoker" and
        chest_pain == "Severe" and
        cholesterol == "High (≥240)"):
        return "Coronary Heart Disease"

    # R4 – Coronary Heart Disease
    if (diabetes == "Yes" and
        blood_pressure == "High" and
        ecg == "Abnormal"):
        return "Coronary Heart Disease"

    # R5 – Hypertensive Heart Disease
    if (blood_pressure == "Persistently Very High" and
        ecg == "High Abnormality" and
        age > 40):
        return "Hypertensive Heart Disease"

    # R6 – Hypertensive Heart Disease
    if (blood_pressure == "High" and
        fatigue == "High" and
        breathing == "Difficulty"):
        return "Hypertensive Heart Disease"

    # R7 – Rheumatic Heart Disease
    if (joint_pain == "Severe" and
        100 < heart_rate < 121 and
        age < 30):
        return "Rheumatic Heart Disease"

    # R8 – Rheumatic Heart Disease
    if (joint_pain == "Present" and
        ecg == "Abnormal" and
        fatigue == "High"):
        return "Rheumatic Heart Disease"

    # R9 – Rheumatic Heart Disease
    if (fever == "Recent" and
        joint_pain == "Severe" and
        murmur == "Yes"):
        return "Rheumatic Heart Disease"

    # R10 – Weak Heart Disease
    if (breathing == "Severe Difficulty" and
        fatigue == "Extreme" and
        heart_rate > 120):
        return "Weak Heart Disease"

    # R11 – Weak Heart Disease
    if (blood_pressure == "Low" and
        breathing == "Difficulty" and
        age > 70):
        return "Weak Heart Disease"

    # R12 – Weak Heart Disease
    if (swelling == "Present" and
        breathing == "Severe Difficulty" and
        fatigue == "Extreme"):
        return "Weak Heart Disease"

    # R13 – Weak Heart Disease
    if (murmur == "Yes" and
        swelling == "Present" and
        blood_pressure == "Low"):
        return "Weak Heart Disease"

    # R14 – Heart Valve Disease
    if (ecg == "Abnormal" and
        breathing == "Difficulty" and
        fatigue == "High" and
        blood_pressure in ["Normal", "Low"]):
        return "Heart Valve Disease"

    # R15 – Heart Valve Disease
    if (heart_rate > 120 and
        breathing == "Difficulty" and
        age > 60):
        return "Heart Valve Disease"

    # R16 – Heart Valve Disease
    if (murmur == "Yes" and
        ecg == "Abnormal" and
        fever == "Past"):
        return "Heart Valve Disease"

    # R17 – Heart Valve Disease
    if (murmur == "Yes" and
        swelling in ["Absent", "Mild"] and
        breathing == "Mild"):
        return "Heart Valve Disease"

    # R18 – Normal Heart
    if (60 < heart_rate < 101 and
        chest_pain == "Absent" and
        blood_pressure == "Normal" and
        ecg == "Normal" and
        cholesterol == "Normal (<200)" and
        breathing == "Normal" and
        fatigue == "Normal" and
        joint_pain == "Absent" and
        fever == "Absent" and
        murmur == "No" and
        swelling == "Absent" and
        smoking == "Non-smoker" and
        diabetes == "No"):
        return "Normal Heart"

    # Default
    return "No clear diagnosis – Further medical evaluation recommended"
