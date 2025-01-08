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
#.................................
class CarBase(BaseModel):
    name: str
    color: str
    plate: str
    ownerId: int

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    plate: Optional[str] = None
    ownerId: Optional[int] = None

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

