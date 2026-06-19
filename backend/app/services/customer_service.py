from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate


# CREATE
def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(name=customer.name, phone_number=customer.phone_number)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# READ ALL
def get_customers(db: Session):
    return db.query(Customer).all()


# READ ONE
def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def update_customer(db: Session, customer_id: int, customer_data: CustomerCreate):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return None

    customer.name = customer_data.name
    customer.phone_number = customer_data.phone_number

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return None

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted successfully"}