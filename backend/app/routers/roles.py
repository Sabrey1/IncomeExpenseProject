from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.role import RoleResponse

from database import get_db
from app.schemas.role import RoleCreate
from app.services import role_service

router = APIRouter()


# CREATE
@router.post("/")
def create(role: RoleCreate, db: Session = Depends(get_db)):
    return role_service.create_role(db, role)


# READ ALL
@router.get("/", response_model=List[RoleResponse])
def read_roles(db: Session = Depends(get_db)):
    return role_service.get_roles(db)


# READ ONE
@router.get("/{role_id}", response_model=RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    return role_service.get_role(db, role_id)


# UPDATE
@router.put("/{role_id}")
def update(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    return role_service.update_role(db, role_id, role)


# DELETE
@router.delete("/{role_id}")
def delete(role_id: int, db: Session = Depends(get_db)):
    return role_service.delete_role(db, role_id)