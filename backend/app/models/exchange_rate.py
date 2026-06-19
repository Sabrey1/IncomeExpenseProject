from sqlalchemy import Column, Integer, String
from database import Base

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    from_currency_id = Column(String(100), unique=True)
    to_currency_id = Column(String(100), nullable = True)
    rate = Column(Integer)