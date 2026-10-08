from pathlib import Path

import joblib
import pandas as pd


from api.config import MODEL_PATH, THRESHOLD_PATH

from api.logger import get_logger

logger = get_logger(__name__)

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

if not THRESHOLD_PATH.exists():
    raise FileNotFoundError(
        f"Threshold file not found: {THRESHOLD_PATH}"
    )


model = joblib.load(MODEL_PATH)

threshold_config = joblib.load(THRESHOLD_PATH)

threshold = threshold_config["threshold"]


def is_model_loaded():
    return model is not None


def predict_churn(customer_data: dict):

    logger.info("Starting churn prediction")

    df = pd.DataFrame([customer_data])

    df = df.rename(columns={
        "senior_citizen": "SeniorCitizen",
        "partner": "Partner",
        "dependents": "Dependents",
        "phone_service": "PhoneService",
        "multiple_lines": "MultipleLines",
        "internet_service": "InternetService",
        "online_security": "OnlineSecurity",
        "online_backup": "OnlineBackup",
        "device_protection": "DeviceProtection",
        "tech_support": "TechSupport",
        "streaming_tv": "StreamingTV",
        "streaming_movies": "StreamingMovies",
        "contract": "Contract",
        "paperless_billing": "PaperlessBilling",
        "payment_method": "PaymentMethod",
        "monthly_charges": "MonthlyCharges",
        "total_charges": "TotalCharges"
    })

    probability = model.predict_proba(df)[0, 1]

    prediction = int(probability >= threshold)

    logger.info(
        "Prediction completed: probability=%.4f, prediction=%d",
        probability,
        prediction
    )

    return {
        "churn_probability": float(probability),
        "prediction": prediction,
        "churn": bool(prediction)
    }


def is_model_loaded():
    return model is not None