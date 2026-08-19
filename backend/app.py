import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from .routes import auth_routes, patient_routes, request_routes, review_routes, code_routes

app = FastAPI(
    title="Prior Authorization System API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

frontend_origin = os.getenv("FRONTEND_ORIGIN", "https://prioraurthazotion-bvhfd2c6a2f2fnht.centralindia-01.azurewebsites.net")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        
        frontend_origin
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(patient_routes.router)
app.include_router(request_routes.router)
app.include_router(review_routes.router)
app.include_router(code_routes.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Prior Authorization API is running"}
