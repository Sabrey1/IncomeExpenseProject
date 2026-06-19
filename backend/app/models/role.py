from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable = True, index=True)
    is_enable = Column(Boolean, default=True)