from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.income_type import IncomeTypeResponse

from database import get_db
from app.schemas.income_type import IncomeTypeCreate
from app.services import income_type_service

router = APIRouter()


# CREATE
@router.post("/")
def create(income_type: IncomeTypeCreate, db: Session = Depends(get_db)):
    return income_type_service.create_income_type(db, income_type)


# READ ALL
@router.get("/", response_model=List[IncomeTypeResponse])
def read_income_types(db: Session = Depends(get_db)):
    return income_type_service.get_income_types(db)


# READ ONE
@router.get("/{income_type_id}", response_model=IncomeTypeResponse)
def read_income_type(income_type_id: int, db: Session = Depends(get_db)):
    return income_type_service.get_income_type(db, income_type_id)


# UPDATE
@router.put("/{income_type_id}")
def update(income_type_id: int, income_type: IncomeTypeCreate, db: Session = Depends(get_db)):
    return income_type_service.update_income_type(db, income_type_id, income_type)


# DELETE
@router.delete("/{income_type_id}")
def delete(income_type_id: int, db: Session = Depends(get_db)):
    return income_type_service.delete_income_type(db, income_type_id)