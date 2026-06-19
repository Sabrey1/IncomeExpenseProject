from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate


# CREATE
def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name, description=role.description, is_enable=role.is_enable)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# READ ALL
def get_roles(db: Session):
    return db.query(Role).all()


# READ ONE
def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()


def update_role(db: Session, role_id: int, role_data: RoleCreate):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        return None

    role.name = role_data.name
    role.description = role_data.description
    role.is_enable = role_data.is_enable

    db.commit()
    db.refresh(role)

    return role


def delete_role(db: Session, role_id: int):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        return None

    db.delete(role)
    db.commit()

    return {"message": "Role deleted successfully"}