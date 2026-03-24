from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    title: str = Field(..., title="Header for Note", max_length=100)
    content: str = Field(..., title="Body Text Content")

class NoteCreate(NoteBase):
    user_id: int = Field(..., title="The Author/User Owner ID")

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, title="Optional Edit Title")
    content: Optional[str] = Field(None, title="Optional Edit Content")

class NoteResponse(NoteBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
