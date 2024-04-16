# main.py

from fastapi import FastAPI
from routes import router as vehicle_router

app = FastAPI()

app.include_router(vehicle_router, prefix="/vehicles")
