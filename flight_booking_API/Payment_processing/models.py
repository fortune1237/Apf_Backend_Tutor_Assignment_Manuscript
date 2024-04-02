from pydantic import BaseModel, field_validator, Field
from datetime import datetime

class PaymentRequest(BaseModel):
    amount: float 
    card_number: str = Field(max_length=16, min_length=16)
    expiration_date: datetime
    cvv: str = Field(max_length=3, min_length=3)


    @field_validator("card_number")
    def validate_card_number(cls, value):
        if not value.isnumeric():
            raise ValueError("Must only contain numbers")
        else:
            return value
        
    @field_validator("cvv")
    def validate_cvv(cls, value):
        if not value.isnumeric():
            raise ValueError("Must only contain numbers")
        return value
        


    @field_validator("expiration_date")
    def validate_date(cls, value):
        if value.date() <= datetime.now().date():
            raise ValueError("Date cannot be in the past")
        return value
