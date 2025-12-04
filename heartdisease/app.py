# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from expert_system import diagnose

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/diagnose", response_class=HTMLResponse)
def get_diagnosis(
    request: Request,
    heart_rate: int = Form(...),
    chest_pain: str = Form(...),
    blood_pressure: int = Form(...),
    age: int = Form(...),
    ecg: str = Form(...),
    cholesterol: int = Form(...),
    blood_sugar: int = Form(...),
    breathing: str = Form(...),
    fatigue: str = Form(...),
    joint_pain: str = Form(...)
):
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
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
