# app/schemas/schemas.py
from pydantic import BaseModel
from typing import Optional
class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
