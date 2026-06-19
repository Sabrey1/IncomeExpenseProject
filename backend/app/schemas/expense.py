from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    expense_type_id: int
    currency_id: int
    title: str
    payment_method_id: int
    amount: int
    note: str


class ExpenseResponse(BaseModel):
    id: int
    expense_type_id: int
    currency_id: int
    title: str
    payment_method_id: int
    amount: int
    note: str


    class Config:
        from_attributes = True