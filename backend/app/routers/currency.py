from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.currency import CurrencyResponse

from database import get_db
from app.schemas.currency import CurrencyCreate
from app.services import currency_service

router = APIRouter()


# CREATE
@router.post("/")
def create(currency: CurrencyCreate, db: Session = Depends(get_db)):
    return currency_service.create_currency(db, currency)


# READ ALL
@router.get("/", response_model=List[CurrencyResponse])
def read_crrencies(db: Session = Depends(get_db)):
    return currency_service.get_currencies(db)


# READ ONE
@router.get("/{currency_id}", response_model=CurrencyResponse)
def read_currency(currency_id: int, db: Session = Depends(get_db)):
    return currency_service.get_customer(db, currency_id)


# UPDATE
@router.put("/{currency_id}")
def update(currency_id: int, currency: CurrencyCreate, db: Session = Depends(get_db)):
    return currency_service.update_customer(db, currency_id, currency)


# DELETE
@router.delete("/{currency_id}")
def delete(currency_id: int, db: Session = Depends(get_db)):
    return currency_service.delete_customer(db, currency_id)