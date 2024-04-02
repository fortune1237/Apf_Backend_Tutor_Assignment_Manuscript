from fastapi import FastAPI
from routes import router as booking_router

app = FastAPI()

# Include routes defined in routes.py
app.include_router(booking_router)
