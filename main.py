from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import os

# --------------------------------------------------
# App Configuration
# --------------------------------------------------

app = FastAPI(
    title="PREDIX - Diabetes Risk API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Load Models
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

stageA_model = joblib.load(os.path.join(BASE_DIR, "stageA_model.pkl"))
stageB_model = joblib.load(os.path.join(BASE_DIR, "stageB_model.pkl"))
FEATURES = joblib.load(os.path.join(BASE_DIR, "feature_list.pkl"))

THRESHOLD_A = 0.22
THRESHOLD_B = 0.50

# --------------------------------------------------
# Request Model
# --------------------------------------------------

class PatientData(BaseModel):
    HighBP: int
    HighChol: int
    CholCheck: int
    BMI: float
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    HvyAlcoholConsump: int
    AnyHealthcare: int
    NoDocbcCost: int
    GenHlth: int
    MentHlth: int
    PhysHlth: int
    DiffWalk: int
    Sex: int
    Age: int
    Education: int
    Income: int
    BMI_Category: int
    Age_Group: int
    Healthy_Diet: int
    Chol_Check_Interaction: int
    HealthBurden: int
    LifestyleRisk: int
    Alcohol: int
   

# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "PREDIX Backend is running successfully"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/predict")
def predict(patient: PatientData):

    try:
        input_df = pd.DataFrame([patient.dict()])
        result = final_predict(input_df)

        # Map prediction
        if result == 0:
            prediction = "Normal"
            risk_score = 20
        elif result == 1:
            prediction = "Prediabetes"
            risk_score = 55
        else:
            prediction = "Diabetes"
            risk_score = 85

        insights = []

        if patient.BMI > 30:
            insights.append("High BMI increases insulin resistance.")

        if patient.HighBP == 1:
            insights.append("High blood pressure increases diabetes risk.")

        if patient.PhysActivity == 0:
            insights.append("Low physical activity contributes to higher risk.")

        if patient.HvyAlcoholConsump == 1:
            insights.append("Heavy alcohol consumption impacts glucose regulation.")

        recommendations = [
            "Maintain balanced diet with low refined sugars.",
            "Engage in at least 30 minutes of daily exercise.",
            "Monitor blood glucose levels regularly.",
            "Schedule routine health checkups."
        ]

        return {
            "prediction": prediction,
            "risk_score": risk_score,
            "insights": insights,
            "recommendations": recommendations
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))