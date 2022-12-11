from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict


app = FastAPI()


class Input(BaseModel):
    precipitation: float
    temp_max: float
    temp_min: float
    wind: float
    month_1: float
    month_2: float
    month_3: float
    month_4: float
    month_5: float
    month_6: float
    month_7: float
    month_8: float
    month_9: float
    month_10: float
    month_11: float
    month_12: float


class PredictionOut(BaseModel):
    weather: str


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict")
def WeatherResult(payload: Input):
    weather = predict(payload.precipitation, payload.temp_max, payload.temp_min, payload.wind, payload.month_1, 
                    payload.month_2, payload.month_3, payload.month_4, payload.month_5, payload.month_6, payload.month_7, 
                    payload.month_8,payload.month_9, payload.month_10, payload.month_11, payload.month_12)
    return {"Result": weather}