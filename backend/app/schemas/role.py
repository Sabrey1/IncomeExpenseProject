from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str
    is_enable: bool


class RoleResponse(BaseModel):
    id: int
    name: str
    description: str
    is_enable: bool

    class Config:
        from_attributes = True