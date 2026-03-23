from pydantic import BaseModel, Field
from database import Base
from datetime import datetime
from typing import Optional

class ArticleBase(BaseModel):
    title: str = Field(...,min_length=1, max_length=200)
    content: str =Field(...,min_length=1)
    author: str =Field(..., min_length=1,max_length=100)
    
    
class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    
    
class ArticleResponse(ArticleBase):
    id : int
    content: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
    
