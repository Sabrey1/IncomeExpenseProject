from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from app.schemas.user import UserCreate
from app.services import user_service

router = APIRouter()


# CREATE
@router.post("/")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


# READ ALL
@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


# READ ONE
@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)


# UPDATE
@router.put("/{user_id}")
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user)


# DELETE
@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)