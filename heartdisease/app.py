from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static folder for CSS if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# -------------------------------
#       DIAGNOSIS ENGINE
# -------------------------------
def diagnose(
    age_group, gender, chest_pain, short_breath, fatigue,
    dizziness, cold_sweat, smoker, diabetes, blood_pressure,
    family_history, inactive
):
    risk_points = 0

    # Age contribution
    if age_group == "Middle-Aged Adult":
        risk_points += 2
    elif age_group == "Elderly":
        risk_points += 3

    # Symptom contribution
    if chest_pain in ["Moderate", "Severe"]:
        risk_points += 3
    if short_breath == "Yes":
        risk_points += 2
    if fatigue == "Yes":
        risk_points += 1
    if dizziness == "Yes":
        risk_points += 1
    if cold_sweat == "Yes":
        risk_points += 1

    # Medical history contribution
    if smoker == "Smoker":
        risk_points += 2
    if diabetes == "Yes":
        risk_points += 2
    if blood_pressure == "Elevated":
        risk_points += 1
    elif blood_pressure == "High":
        risk_points += 3
    if family_history == "Yes":
        risk_points += 2
    if inactive == "Physically Inactive":
        risk_points += 1

    # Determine risk level based on points
    if risk_points >= 10:
        return "High"
    elif risk_points >= 5:
        return "Moderate"
    else:
        return "Low"

# -------------------------------
#    RECOMMENDATIONS ENGINE
# -------------------------------
def recommendation(risk_level):
    rec = {
        "High": "Consult a cardiologist immediately, monitor your vitals, maintain a heart-healthy diet, avoid smoking, and schedule follow-up tests.",
        "Moderate": "Schedule a checkup with your doctor, follow a balanced diet, exercise moderately, avoid smoking, and monitor your vitals.",
        "Low": "Maintain regular exercise and a healthy diet, monitor your vitals, avoid smoking, and have routine health checkups."
    }
    return rec.get(risk_level, "")

# -------------------------------
#       ROUTES
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    age_group: str = Form(...),
    gender: str = Form(...),
    chest_pain: str = Form(...),
    short_breath: str = Form(...),
    fatigue: str = Form(...),
    dizziness: str = Form(...),
    cold_sweat: str = Form(...),
    smoker: str = Form(...),
    diabetes: str = Form(...),
    blood_pressure: str = Form(...),
    family_history: str = Form(...),
    inactive: str = Form(...),
):
    # Diagnose risk
    risk_level = diagnose(
        age_group, gender, chest_pain, short_breath, fatigue,
        dizziness, cold_sweat, smoker, diabetes, blood_pressure,
        family_history, inactive
    )

    # Get recommendation
    advice = recommendation(risk_level)

    # Prepare inputs dictionary for summary table
    inputs = {
        "age_group": age_group,
        "gender": gender,
        "chest_pain": chest_pain,
        "short_breath": short_breath,
        "fatigue": fatigue,
        "dizziness": dizziness,
        "cold_sweat": cold_sweat,
        "smoker": smoker,
        "diabetes": diabetes,
        "blood_pressure": blood_pressure,
        "family_history": family_history,
        "inactive": inactive
    }

    return templates.TemplateResponse("result.html", {
        "request": request,
        "risk_level": risk_level,
        "recommendation": advice,
        "inputs": inputs
    })

# Run with:
# uvicorn app:app --reload
