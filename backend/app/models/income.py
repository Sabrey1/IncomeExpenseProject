from sqlalchemy import Column, Integer, String
from database import Base

class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    income_type_id = Column(Integer, unique=True)
    currency_id = Column(Integer, nullable = True)
    title = Column(String(100))
    amount = Column(Integer)
    payment_method_id = Column(Integer)
    note = Column(String(100))