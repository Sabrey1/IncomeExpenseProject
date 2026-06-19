from pydantic import BaseModel

class ExpenseTypeCreate(BaseModel):
    name: str
    description: str


class ExpenseTypeResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True