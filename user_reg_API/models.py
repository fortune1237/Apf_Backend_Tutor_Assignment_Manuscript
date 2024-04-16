from pydantic import BaseModel, EmailStr, Field

class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)
