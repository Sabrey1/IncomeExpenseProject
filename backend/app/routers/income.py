from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.income import IncomeResponse

from database import get_db
from app.schemas.income import IncomeCreate
from app.services import income_service

router = APIRouter()


# CREATE
@router.post("/")
def create(income: IncomeCreate, db: Session = Depends(get_db)):
    return income_service.create_income(db, income)


# READ ALL
@router.get("/", response_model=List[IncomeResponse])
def read_incomes(db: Session = Depends(get_db)):
    return income_service.get_incomes(db)


# READ ONE
@router.get("/{income_id}", response_model=IncomeResponse)
def read_income(income_id: int, db: Session = Depends(get_db)):
    return income_service.get_income(db, income_id)


# UPDATE
@router.put("/{income_id}")
def update(income_id: int, income: IncomeCreate, db: Session = Depends(get_db)):
    return income_service.update_income(db, income_id, income)


# DELETE
@router.delete("/{income_id}")
def delete(income_id: int, db: Session = Depends(get_db)):
    return income_service.delete_income(db, income_id)