from fastapi import APIRouter, HTTPException, Body
from models import UserRegistration
from services import register_user
from pydantic import ValidationError

router = APIRouter()

@router.post("/register")
async def register(user: UserRegistration = Body(...)):
    try:
        register_user(user)
        return {"message": "User registered successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
