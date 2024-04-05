from models import UserRegistration
from fastapi import HTTPException

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
