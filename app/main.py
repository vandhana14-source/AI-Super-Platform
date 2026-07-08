from fastapi import FastAPI

app = FastAPI(
    title="AI Super Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Super Platform 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "Running Successfully"
    }

from app.database import engine, Base

Base.metadata.create_all(bind=engine)