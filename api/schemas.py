from pydantic import BaseModel, Field


class CustomerRequest(BaseModel):
    gender: str
    senior_citizen: int = Field(ge=0, le=1)
    partner: str
    dependents: str
    tenure: int = Field(ge=0, le=72)
    phone_service: str
    multiple_lines: str
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str
    contract: str
    paperless_billing: str
    payment_method: str
    monthly_charges: float = Field(gt=0)
    total_charges: float = Field(ge=0)


class PredictionResponse(BaseModel):
    churn_probability: float
    prediction: int
    churn: bool