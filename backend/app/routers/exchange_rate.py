from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.exchange_rate import ExchangeRateResponse

from database import get_db
from app.schemas.exchange_rate import ExchangeRateCreate
from app.services import exchange_rate_service

router = APIRouter()


# CREATE
@router.post("/")
def create(exchange_rate: ExchangeRateCreate, db: Session = Depends(get_db)):
    return exchange_rate_service.create_exchange_rate(db, exchange_rate)


# READ ALL
@router.get("/", response_model=List[ExchangeRateResponse])
def read_exchange_rates(db: Session = Depends(get_db)):
    return exchange_rate_service.get_exchange_rates(db)


# READ ONE
@router.get("/{exchange_rate_id}", response_model=ExchangeRateResponse)
def read_exchange_rate(exchange_rate_id: int, db: Session = Depends(get_db)):
    return exchange_rate_service.get_exchange_rate(db, exchange_rate_id)


# UPDATE
@router.put("/{exchange_rate_id}")
def update(exchange_rate_id: int, customer: ExchangeRateCreate, db: Session = Depends(get_db)):
    return exchange_rate_service.update_exchange_rate(db, exchange_rate_id, customer)


# DELETE
@router.delete("/{exchange_rate_id}")
def delete(exchange_rate_id: int, db: Session = Depends(get_db)):
    return exchange_rate_service.delete_exchange_rate(db, exchange_rate_id)