from sqlalchemy.orm import Session
from app.models.expense_type import ExpenseType
from app.schemas.expense_type import ExpenseTypeCreate


# CREATE
def create_expense_type(db: Session, expense_type: ExpenseTypeCreate):
    db_expense_type = ExpenseType(**expense_type.dict())
    db.add(db_expense_type)
    db.commit()
    db.refresh(db_expense_type)
    return db_expense_type


# READ ALL
def get_expenses_types(db: Session):
    return db.query(ExpenseType).all()


# READ ONE
def get_expense_type(db: Session, expense_type_id: int):
    return db.query(ExpenseType).filter(ExpenseType.id == expense_type_id).first()


def update_expense_type(db: Session, expense_type_id: int, expense_type_data: ExpenseTypeCreate):
    expense_type = db.query(ExpenseType).filter(ExpenseType.id == expense_type_id).first()

    if not expense_type:
        return None

    expense_type.name = expense_type_data.name
    expense_type.description = expense_type_data.description

    db.commit()
    db.refresh(expense_type)

    return expense_type


def delete_expense_type(db: Session, expense_type_id: int):
    expense_type = db.query(ExpenseType).filter(ExpenseType.id == expense_type_id).first()

    if not expense_type:
        return None

    db.delete(expense_type)
    db.commit()

    return {"message": "Expense Type deleted successfully"}