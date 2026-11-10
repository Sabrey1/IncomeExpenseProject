from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    role_id: int
    is_active: int

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role_id: Optional[int] = None
    is_active: Optional[int] = None

    class Config:
        from_attributes = True