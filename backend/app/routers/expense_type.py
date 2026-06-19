from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.expense_type import ExpenseTypeResponse

from database import get_db
from app.schemas.expense_type import ExpenseTypeCreate
from app.services import expense_type_service

router = APIRouter()


# CREATE
@router.post("/")
def create(expense_type: ExpenseTypeCreate, db: Session = Depends(get_db)):
    return expense_type_service.create_expense_type(db, expense_type)


# READ ALL
@router.get("/", response_model=List[ExpenseTypeResponse])
def read_expense_types(db: Session = Depends(get_db)):
    return expense_type_service.get_expense_types(db)


# READ ONE
@router.get("/{expense_type_id}", response_model=ExpenseTypeResponse)
def read_expense_type(expense_type_id: int, db: Session = Depends(get_db)):
    return expense_type_service.get_expense_type(db, expense_type_id)


# UPDATE
@router.put("/{expense_type_id}")
def update(expense_type_id: int, expense_type: ExpenseTypeCreate, db: Session = Depends(get_db)):
    return expense_type_service.update_expense_type(db, expense_type_id, expense_type)


# DELETE
@router.delete("/{expense_type_id}")
def delete(expense_type_id: int, db: Session = Depends(get_db)):
    return expense_type_service.delete_expense_type(db, expense_type_id)