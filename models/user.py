from pydantic import BaseModel

class User(BaseModel):
    name: str  
    email: str
    password: str
    city: str
    pincode: int
    mobile_no: int
