from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class UserOut(BaseModel):
    id: int
    email: EmailStr
    phone: str
    name: str
    # created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone: str
    name: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    stars: int
    img: str
    location: str
    type_id: int

    class Config:
        orm_mode = True


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: int
    stars: int
    img: str
    location: str
    created_at: datetime
    updated_at: datetime
    type_id: int

    class Config:
        orm_mode = True


class AddressCreate(BaseModel):
    addressType: str
    contactPersonName: str
    contactPersonNumber: int
    address: str
    latitude: str
    longitude: str

    class Config:
        orm_mode = True

class AddressCordinates(BaseModel):
    latitude: str
    longitude: str

    class Config:
        orm_mode = True
