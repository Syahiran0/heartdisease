import streamlit as st
from expert_system import diagnose

# Page config
st.set_page_config(page_title="Heart Attack Risk Pre-Screening", layout="centered")

# Title
st.title("❤️ Heart Attack Risk Pre-Screening")
st.write("Fill in your details to check your heart risk.")

# Inputs
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=70)
chest_pain = st.selectbox("Chest Pain", ["none", "mild", "severe", "painful"])
blood_pressure = st.number_input("Blood Pressure", min_value=80, max_value=200, value=120)
age = st.number_input("Age", min_value=1, max_value=120, value=30)
ecg = st.selectbox("ECG", ["normal", "abnormal", "irregular"])
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400, value=180)
blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=50, max_value=400, value=100)
breathing = st.selectbox("Breathing", ["normal", "short"])
fatigue = st.selectbox("Fatigue Level", ["low", "high"])
joint_pain = st.selectbox("Joint Pain", ["none", "present", "severe"])

# Button
if st.button("Check Risk"):
    inputs = {
        "heart_rate": heart_rate,
        "chest_pain": chest_pain,
        "blood_pressure": blood_pressure,
        "age": age,
        "ecg": ecg,
        "cholesterol": cholesterol,
        "blood_sugar": blood_sugar,
        "breathing": breathing,
        "fatigue": fatigue,
        "joint_pain": joint_pain
    }

    result = diagnose(inputs)
    st.success(f"Diagnosis: {result}")
