from sqlalchemy.orm import Session
from app.models.currency import Currency
from app.schemas.currency import CurrencyCreate


# CREATE
def create_currency(db: Session, currency: CurrencyCreate):
    db_currency = Currency(code=currency.code, symbol=currency.symbol, is_default=currency.is_default)
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


# READ ALL
def get_currencies(db: Session):
    return db.query(Currency).all()


# READ ONE
def get_currency(db: Session, currency_id: int):
    return db.query(Currency).filter(Currency.id == currency_id).first()


def update_currency(db: Session, currency_id: int, currency_data: CurrencyCreate):
    currency = db.query(currency).filter(currency.id == currency_id).first()

    if not currency:
        return None

    currency.code = currency_data.code
    currency.symbol = currency_data.symbol
    currency.is_default = currency_data.is_default

    db.commit()
    db.refresh(currency)

    return currency


def delete_currency(db: Session, currency_id: int):
    currency = db.query(Currency).filter(Currency.id == currency_id).first()

    if not currency:
        return None

    db.delete(currency)
    db.commit()

    return {"message": "Currency deleted successfully"}