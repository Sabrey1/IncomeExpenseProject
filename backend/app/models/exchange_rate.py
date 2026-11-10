from sqlalchemy import Column, Integer, ForeignKey, Numeric
from database import Base
from sqlalchemy.orm import relationship

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    from_currency_id = Column(
        Integer,
        ForeignKey("currencies.id"),
        nullable=False
    )

    to_currency_id = Column(
        Integer,
        ForeignKey("currencies.id"),
        nullable=False
    )
    rate = Column(Numeric(18, 8), nullable=False)
    from_currency = relationship(
        "Currency",
        foreign_keys=[from_currency_id]
    )

    to_currency = relationship(
        "Currency",
        foreign_keys=[to_currency_id]
    )