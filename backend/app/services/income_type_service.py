from sqlalchemy.orm import Session
from app.models.income_type import IncomeType
from app.schemas.income_type import IncomeTypeCreate


# CREATE
def create_income_type(db: Session, income_type: IncomeTypeCreate):
    db_income_type = IncomeType(**income_type.dict())
    db.add(db_income_type)
    db.commit()
    db.refresh(db_income_type)
    return db_income_type


# READ ALL
def get_income_types(db: Session):
    return db.query(IncomeType).all()


# READ ONE
def get_income_type(db: Session, income_type_id: int):
    return db.query(IncomeType).filter(IncomeType.id == income_type_id).first()


def update_income_type(db: Session, income_type_id: int, income_type_data: IncomeTypeCreate):
    income_type = db.query(IncomeType).filter(IncomeType.id == income_type_id).first()

    if not income_type:
        return None

    income_type.name = income_type_data.name
    income_type.description = income_type_data.description

    db.commit()
    db.refresh(income_type)

    return income_type


def delete_income_type(db: Session, income_type_id: int):
    income_type = db.query(IncomeType).filter(IncomeType.id == income_type_id).first()

    if not income_type:
        return None

    db.delete(income_type)
    db.commit()

    return {"message": "Income Type deleted successfully"}