from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), unique=True)
    symbol = Column(String(100), nullable = True)
    is_default = Column(Boolean, default=True)