from pydantic import BaseModel

class IncomeTypeCreate(BaseModel):
    name: str
    description: str


class IncomeTypeResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True