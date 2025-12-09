from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

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
#       ROUTES
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    heart_rate: int = Form(...),
    chest_pain: str = Form(...),
    blood_pressure: str = Form(...),
    age: int = Form(...),
    ecg: str = Form(...),
    cholesterol: int = Form(...),
    breathing: str = Form(...),
    fatigue: str = Form(...),
    joint_pain: str = Form(...),
    fever_history: str = Form(...),
    murmur: str = Form(...),
    swelling: str = Form(...),
    smoking: str = Form(...),
    diabetes: str = Form(...),
):
    diagnosis_result = diagnose(
        heart_rate, chest_pain, blood_pressure, age, ecg, cholesterol,
        breathing, fatigue, joint_pain, fever_history, murmur,
        swelling, smoking, diabetes
    )

    advice = recommendation(diagnosis_result)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "diagnosis": diagnosis_result,
        "recommendation": advice
    })
