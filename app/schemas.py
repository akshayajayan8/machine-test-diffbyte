from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserCreate(BaseModel):
    name:str = Field(..., max_length=200)
    email:EmailStr
    message:str = Field(..., max_length=500)