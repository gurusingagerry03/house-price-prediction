from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="House Price Predictor API")

# Load model and RMSE
try:
    loaded = joblib.load("house_price_model.pkl")
    model = loaded["model"]
    rmse = loaded["rmse"]
except Exception as e:
    print("❌ Gagal load model:", e)
    model = None
    rmse = 0

# Input schema
class HouseInput(BaseModel):
    GrLivArea: float
    BedroomAbvGr: int
    FullBath: int
    GarageCars: int
    YearBuilt: int

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: HouseInput):
    if model is None:
        return {"error": "Model not loaded"}
    
    X = np.array([[data.GrLivArea, data.BedroomAbvGr, data.FullBath, data.GarageCars, data.YearBuilt]])
    prediction = model.predict(X)[0]
    min_estimate = max(0, prediction - rmse)
    max_estimate = prediction + rmse

    return {
        "predicted_price": int(prediction),
        "min_estimate": int(min_estimate),
        "max_estimate": int(max_estimate)
    }
