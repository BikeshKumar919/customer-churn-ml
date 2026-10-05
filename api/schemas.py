from pydantic import BaseModel, Field


class CustomerRequest(BaseModel):
    gender: str
    senior_citizen: int = Field(ge=0, le=1)
    tenure: int = Field(ge=0, le=72)
    monthly_charges: float = Field(gt=0)