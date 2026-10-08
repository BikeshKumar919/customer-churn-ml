from fastapi import FastAPI, HTTPException

from api.config import settings
from api.logger import get_logger
from api.schemas import CustomerRequest, PredictionResponse
from api.model_service import is_model_loaded, predict_churn


logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="ML API for predicting customer churn",
    version=settings.app_version
)

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "model_loaded": is_model_loaded()
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(customer: CustomerRequest):

    logger.info("Prediction request received")

    try:
        result = predict_churn(
            customer.model_dump()
        )

        return result

    except Exception as e:

        logger.exception("Prediction failed")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )