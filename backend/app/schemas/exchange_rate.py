from decimal import Decimal

from app.schemas.currency import CurrencySimple
from pydantic import BaseModel

class ExchangeRateCreate(BaseModel):
    from_currency_id: int
    to_currency_id: int
    rate: Decimal

class ExchangeRateResponse(BaseModel):
    id: int
    from_currency: str
    to_currency: str
    rate: Decimal

    class Config:
        from_attributes = True