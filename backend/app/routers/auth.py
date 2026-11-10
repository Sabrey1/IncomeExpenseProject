from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from app.services import auth_service

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return auth_service.login(db, username, password)