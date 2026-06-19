from sqlalchemy.orm import Session
from app.models.payment_method import PaymentMethod
from app.schemas.payment_method import PaymentMethodCreate


# CREATE
def create_payment_method(db: Session, payment_method: PaymentMethodCreate):
    db_payment_method = PaymentMethod(name=payment_method.name)
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method


# READ ALL
def get_payment_methods(db: Session):
    return db.query(PaymentMethod).all()


# READ ONE
def get_payment_method(db: Session, payment_method_id: int):
    return db.query(PaymentMethod).filter(PaymentMethod.id == payment_method_id).first()


def update_payment_method(db: Session, payment_method_id: int, payment_method_data: PaymentMethodCreate):
    payment_method = db.query(PaymentMethod).filter(PaymentMethod.id == payment_method_id).first()

    if not payment_method:
        return None

    payment_method.name = payment_method_data.name

    db.commit()
    db.refresh(payment_method)

    return payment_method


def delete_payment_method(db: Session, payment_method_id: int):
    payment_method = db.query(PaymentMethod).filter(PaymentMethod.id == payment_method_id).first()

    if not payment_method:
        return None

    db.delete(payment_method)
    db.commit()

    return {"message": "Payment method deleted successfully"}