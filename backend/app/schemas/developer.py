from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class DeveloperBase(BaseModel):
    name: str
    email: EmailStr

class DeveloperCreate(DeveloperBase):
    pass

class DeveloperUpdate(DeveloperBase):
    avatar_url: Optional[HttpUrl] = None

class DeveloperInDB(DeveloperBase):
    id: int
    avatar_url: HttpUrl

    class Config:
        orm_mode = True
