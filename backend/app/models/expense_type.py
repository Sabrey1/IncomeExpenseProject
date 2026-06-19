from sqlalchemy import Column, Integer, String
from database import Base

class ExpenseType(Base):
    __tablename__ = "expense_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable = True)