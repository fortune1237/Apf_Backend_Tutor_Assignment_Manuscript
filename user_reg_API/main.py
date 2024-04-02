import uvicorn
from fastapi import FastAPI, HTTPException, Body
from models import UserRegistration
from typing import Optional
from fastapi.testclient import TestClient
from pydantic import ValidationError

app = FastAPI()

def is_password_strong(password: str) -> bool:
    # Check if password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    return has_uppercase and has_lowercase and has_digit and has_special

def register_user(user: UserRegistration):
    if not is_password_strong(user.password):
        raise HTTPException(status_code=422, detail="Password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
    # Here you would perform database operations or other necessary actions to register the user
    # For demonstration purposes, let's just print the user details
    print("User registered:", user.dict())

@app.post("/register")
async def register(user: UserRegistration = Body(...)):
    try:
        register_user(user)
        return {"message": "User registered successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
