from sqlalchemy import Column, Integer, String
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    expense_type_id = Column(Integer)
    currency_id = Column(Integer)
    title = Column(String(100))
    payment_method_id = Column(Integer)
    amount = Column(Integer)
    note = Column(String(100))