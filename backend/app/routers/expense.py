from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.expense import ExpenseResponse

from database import get_db
from app.schemas.expense import ExpenseCreate
from app.services import expense_service

router = APIRouter()


# CREATE
@router.post("/")
def create(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return expense_service.create_expense(db, expense)


# READ ALL
@router.get("/", response_model=List[ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    return expense_service.get_expenses(db)


# READ ONE
@router.get("/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    return expense_service.get_expense(db, expense_id)


# UPDATE
@router.put("/{expense_id}")
def update(expense_id: int, expense: ExpenseCreate, db: Session = Depends(get_db)):
    return expense_service.update_expense(db, expense_id, expense)


# DELETE
@router.delete("/{expense_id}")
def delete(expense_id: int, db: Session = Depends(get_db)):
    return expense_service.delete_expense(db, expense_id)