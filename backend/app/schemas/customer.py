from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone_number: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone_number: str

    class Config:
        from_attributes = True