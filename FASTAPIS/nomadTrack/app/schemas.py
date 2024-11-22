from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date


class ChecklistBase(BaseModel):
    name: str
    description: Optional[str] = None
    user_id: int


class ChecklistCreate(ChecklistBase):
    pass


class Checklist(ChecklistBase):
    id: int

    class Config:
        orm_mode = True


class TravelBase(BaseModel):
    name: str
    country: str
    city: str
    description: Optional[str] = None


class TravelCreate(TravelBase):
    checklist_ids: List[int] = []
    user_id: int


class Travel(TravelBase):
    id: int
    checklists: List[Checklist] = []

    class Config:
        orm_mode = True


class Checking(BaseModel):
    date: date
    visit: Optional[str] = "Visited On"
    travel_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


# Schema for creating a user
class UserCreate(UserBase):
    password: str  # This will be the plain text password provided by the user


# Response schema for User
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
