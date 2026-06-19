from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate


# CREATE
def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


# READ ALL
def get_expenses(db: Session):
    return db.query(Expense).all()


# READ ONE
def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()


def update_expense(db: Session, expense_id: int, expense_data: ExpenseCreate):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        return None

    expense.expense_type_id = expense_data.expense_type_id
    expense.currency_id = expense_data.currency_id
    expense.title = expense_data.title
    expense.payment_method_id = expense_data.payment_method_id
    expense.amount = expense_data.amount
    expense.note = expense_data.note

    db.commit()
    db.refresh(expense)

    return expense


def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        return None

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}