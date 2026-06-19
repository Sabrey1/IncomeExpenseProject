from pydantic import BaseModel

class ExchangeRateCreate(BaseModel):
    from_currency_id: int
    to_currency_id: int
    rate: int


class ExchangeRateResponse(BaseModel):
    id: int
    from_currency_id: int
    to_currency_id: int
    rate: int

    class Config:
        from_attributes = True