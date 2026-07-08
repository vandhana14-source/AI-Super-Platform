from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Super Platform",
    version="1.0.0",
    description="AI Super Platform Backend"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class ChatRequest(BaseModel):
    message: str

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Super Platform 🚀"
    }

# Health Check API
@app.get("/health")
def health():
    return {
        "status": "Running Successfully"
    }

# Test API
@app.get("/hello")
def hello():
    return {
        "message": "Hello from AI Super Platform!"
    }

# Chat API
@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": f"You said: {request.message}"
    }