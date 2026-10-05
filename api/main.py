from fastapi import FastAPI
from schemas import CustomerRequest

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}!"
    }




@app.post("/customer")
def create_customer(customer: CustomerRequest):
    return {
        "message": "Customer received",
        "customer": customer
    }