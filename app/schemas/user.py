from pydantic import BaseModel, Field
from typing import List, Optional

class UserBase(BaseModel):
    username: str = Field(..., title="Unique Handle Name", min_length=3, max_length=50)
    email: str = Field(..., title="Contact Address")

class UserCreate(UserBase):
    password: str = Field(..., title="Raw Password", min_length=6)

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True # updated for Pydantic v2
