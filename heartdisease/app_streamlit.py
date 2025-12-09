import streamlit as st

# -------------------------------
#       DIAGNOSIS ENGINE
# -------------------------------
def diagnose(
    heart_rate, chest_pain, blood_pressure, age, ecg, cholesterol,
    breathing, fatigue, joint_pain, fever_history, murmur,
    swelling, smoking, diabetes
):
    # CORONARY HEART DISEASE
    if chest_pain == "Severe" and ecg == "Abnormal" and cholesterol >= 240:
        return "Coronary Heart Disease"
    if age > 60 and blood_pressure == "High" and 100 < heart_rate < 121:
        return "Coronary Heart Disease"
    if smoking == "Smoker" and chest_pain == "Severe" and cholesterol >= 240:
        return "Coronary Heart Disease"
    if diabetes == "Yes" and blood_pressure == "High" and ecg == "Abnormal":
        return "Coronary Heart Disease"

    # HYPERTENSIVE HEART DISEASE
    if blood_pressure == "Very High" and ecg == "Abnormally High" and age > 40:
        return "Hypertensive Heart Disease"
    if blood_pressure == "High" and fatigue == "High" and breathing == "Difficult":
        return "Hypertensive Heart Disease"

    # RHEUMATIC HEART DISEASE
    if joint_pain == "Severe" and 100 < heart_rate < 121 and age < 30:
        return "Rheumatic Heart Disease"
    if joint_pain == "Present" and ecg == "Abnormal" and fatigue == "High":
        return "Rheumatic Heart Disease"
    if fever_history == "Recent" and joint_pain == "Severe" and murmur == "Yes":
        return "Rheumatic Heart Disease"

    # WEAK HEART DISEASE
    if breathing == "Severe Difficulty" and fatigue == "Extreme" and heart_rate > 120:
        return "Weak Heart Disease"
    if blood_pressure == "Low" and breathing == "Difficult" and age > 70:
        return "Weak Heart Disease"
    if swelling == "Present" and breathing == "Severe Difficulty" and fatigue == "Extreme":
        return "Weak Heart Disease"
    if murmur == "Yes" and swelling == "Present" and blood_pressure == "Low":
        return "Weak Heart Disease"

    # HEART VALVE DISEASE
    if ecg == "Abnormal" and breathing == "Difficult" and fatigue == "High" and blood_pressure in ["Normal", "Low"]:
        return "Heart Valve Disease"
    if heart_rate > 120 and breathing == "Difficult" and age > 60:
        return "Heart Valve Disease"
    if murmur == "Yes" and ecg == "Abnormal" and fever_history == "Past":
        return "Heart Valve Disease"
    if murmur == "Yes" and swelling in ["Absent", "Mild"] and breathing == "Mild":
        return "Heart Valve Disease"

    # NORMAL HEART
    if (60 < heart_rate < 101 and chest_pain == "Absent" and blood_pressure == "Normal"
        and ecg == "Normal" and cholesterol < 200 and breathing == "Normal"
        and fatigue == "Normal" and joint_pain == "Absent"
        and fever_history == "Absent" and murmur == "No"
        and swelling == "Absent" and smoking == "Non-smoker"
        and diabetes == "No"):
        return "Normal Heart"

    return "Unable to Determine – More Tests Needed"


# -------------------------------
#    RECOMMENDATIONS ENGINE
# -------------------------------
def recommendation(diagnosis):
    rec = {
        "Coronary Heart Disease": "Consult a cardiologist immediately. Maintain a heart-healthy diet, exercise, and take prescribed medications.",
        "Hypertensive Heart Disease": "Monitor blood pressure regularly, reduce salt intake, exercise moderately, and follow your doctor's advice.",
        "Rheumatic Heart Disease": "Visit a cardiologist and check for valve damage. Complete prescribed antibiotics if infection-related and monitor joint pain.",
        "Weak Heart Disease": "Avoid strenuous activity, follow a balanced diet, and consult a cardiologist for further tests and monitoring.",
        "Heart Valve Disease": "Consult a cardiologist for echocardiogram and valve assessment. Follow prescribed medications and lifestyle adjustments.",
        "Normal Heart": "Maintain a healthy lifestyle with regular exercise, balanced diet, and routine health checkups.",
        "Unable to Determine – More Tests Needed": "Consult a doctor for detailed evaluation and further tests."
    }
    return rec.get(diagnosis, "Consult a doctor for further advice.")


# -------------------------------
#       STREAMLIT APP
# -------------------------------
st.set_page_config(page_title="Heart Disease Expert System", page_icon="❤️", layout="centered")
st.title("🫀 Heart Disease Expert System")

st.write("Fill in the patient information below to get a diagnosis and recommendation.")

# Input fields
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=70)
chest_pain = st.selectbox("Chest Pain", ["Absent", "Mild", "Moderate", "Severe"])
blood_pressure = st.selectbox("Blood Pressure", ["Low", "Normal", "High", "Very High", "Persistently Very High"])
age = st.number_input("Patient Age", min_value=1, max_value=120, value=40)
ecg = st.selectbox("ECG", ["Normal", "Abnormal", "Abnormally High", "Irregular Pattern"])
cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=180)
breathing = st.selectbox("Breathing Condition", ["Normal", "Difficult", "Severe Difficulty", "Mild"])
fatigue = st.selectbox("Fatigue Level", ["Normal", "High", "Extreme"])
joint_pain = st.selectbox("Joint Pain", ["Absent", "Present", "Severe"])
fever_history = st.selectbox("History of Fever/Infection", ["Absent", "Recent", "Past"])
murmur = st.selectbox("Heart Murmur Presence", ["No", "Yes"])
swelling = st.selectbox("Ankle/Leg Swelling", ["Absent", "Mild", "Present"])
smoking = st.selectbox("Smoking Status", ["Non-smoker", "Smoker"])
diabetes = st.selectbox("Diabetes Mellitus", ["No", "Yes"])

# Predict button
if st.button("Diagnose"):
    diagnosis_result = diagnose(
        heart_rate, chest_pain, blood_pressure, age, ecg, cholesterol,
        breathing, fatigue, joint_pain, fever_history, murmur,
        swelling, smoking, diabetes
    )
    advice = recommendation(diagnosis_result)
    
    st.subheader("Diagnosis Result")
    st.success(diagnosis_result)
    st.subheader("Recommendation")
    st.info(advice)
