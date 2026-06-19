from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.payment_method import PaymentMethodResponse

from database import get_db
from app.schemas.payment_method import PaymentMethodCreate
from app.services import payment_method_service

router = APIRouter()


# CREATE
@router.post("/")
def create(payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    return payment_method_service.create_payment_method(db, payment_method)


# READ ALL
@router.get("/", response_model=List[PaymentMethodResponse])
def read_payment_methods(db: Session = Depends(get_db)):
    return payment_method_service.get_payment_methods(db)


# READ ONE
@router.get("/{payement_method_id}", response_model=PaymentMethodResponse)
def read_payment_method(payement_method_id: int, db: Session = Depends(get_db)):
    return payment_method_service.get_payment_method(db, payement_method_id)


# UPDATE
@router.put("/{payement_method_id}")
def update(payement_method_id: int, payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    return payment_method_service.update_payment_method(db, payement_method_id, payment_method)


# DELETE
@router.delete("/{payement_method_id}")
def delete(payement_method_id: int, db: Session = Depends(get_db)):
    return payment_method_service.delete_payment_method(db, payement_method_id)