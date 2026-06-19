from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


# CREATE
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# READ ALL
def get_users(db: Session):
    return db.query(User).all()


# READ ONE
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# UPDATE
def update_user(db: Session, user_id: int, user_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = user_data.username
        user.email = user_data.email
        db.commit()
        db.refresh(user)
    return user


# DELETE
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def login(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username and User.password == password).first()

    if not user:
        return {
            "success": False,
            "message": "Invalid username or password",
            "data": None
        }
   
    return {
        "success": True,
        "message": "Login successfully",
        "data": user
    }