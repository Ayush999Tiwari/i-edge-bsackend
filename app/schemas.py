from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserData(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    services_access: List[str]