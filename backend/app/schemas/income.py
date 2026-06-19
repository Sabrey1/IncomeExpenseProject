from pydantic import BaseModel

class IncomeCreate(BaseModel):
    income_type_id: int
    currency_id: int
    title: str
    payment_method_id: int
    amount: int
    note: str


class IncomeResponse(BaseModel):
    id: int
    income_type_id: int
    currency_id: int
    title: str
    payment_method_id: int
    amount: int
    note: str


    class Config:
        from_attributes = True