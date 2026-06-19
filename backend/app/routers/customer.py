from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.customer import CustomerResponse

from database import get_db
from app.schemas.customer import CustomerCreate
from app.services import customer_service

router = APIRouter()


# CREATE
@router.post("/")
def create(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)


# READ ALL
@router.get("/", response_model=List[CustomerResponse])
def read_customers(db: Session = Depends(get_db)):
    return customer_service.get_customers(db)


# READ ONE
@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_service.get_customer(db, customer_id)


# UPDATE
@router.put("/{customer_id}")
def update(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.update_customer(db, customer_id, customer)


# DELETE
@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    return customer_service.delete_customer(db, customer_id)