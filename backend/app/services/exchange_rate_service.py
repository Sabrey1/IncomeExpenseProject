from sqlalchemy.orm import Session
from app.models.exchange_rate import ExchangeRate
from app.schemas.exchange_rate import ExchangeRateCreate


# CREATE
def create_exchange_rate(db: Session, exchange_rate: ExchangeRateCreate):
    db_exchange_rate = ExchangeRate(from_currency_id = exchange_rate.from_currency_id, to_currency_id = exchange_rate.to_currency_id, rate = exchange_rate.rate)
    db.add(db_exchange_rate)
    db.commit()
    db.refresh(db_exchange_rate)
    return db_exchange_rate


# READ ALL
def get_exchange_rates(db: Session):
    return db.query(ExchangeRate).all()


# READ ONE
def get_exchange_rate(db: Session, exchange_rate_id: int):
    return db.query(ExchangeRate).filter(ExchangeRate.id == exchange_rate_id).first()


def update_exchange_rate(db: Session, exchange_rate_id: int, exchange_rate_data: ExchangeRateCreate):
    exchange_rate = db.query(ExchangeRate).filter(ExchangeRate.id == exchange_rate_id).first()

    if not exchange_rate:
        return None

    exchange_rate.from_currency_id = exchange_rate_data.from_currency_id
    exchange_rate.to_currency_id = exchange_rate_data.to_currency_id
    exchange_rate.rate = exchange_rate_data.rate

    db.commit()
    db.refresh(exchange_rate)

    return exchange_rate


def delete_exchange_rate(db: Session, exchange_rate_id: int):
    exchange_rate = db.query(ExchangeRate).filter(ExchangeRate.id == exchange_rate_id).first()

    if not exchange_rate:
        return None

    db.delete(exchange_rate)
    db.commit()

    return {"message": "Exchange rate deleted successfully"}