from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=200)
    author_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)