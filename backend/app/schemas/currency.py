from pydantic import BaseModel

class CurrencyCreate(BaseModel):
    code: str
    symbol: str
    is_default: bool


class CurrencyResponse(BaseModel):
    id: int
    code: str
    symbol: str
    is_default: bool

    class Config:
        from_attributes = True