from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import (
    verify_password,
    create_access_token
)

def login(db: Session, username: str, password: str):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Invalid username or password",
            "data": None
        }

    if not user.is_active:
        return {
            "success": False,
            "message": "User account is inactive",
            "data": None
        }

    if not verify_password(password, user.password):
        return {
            "success": False,
            "message": "Invalid username or password",
            "data": None
        }

    access_token = create_access_token({
        "sub": str(user.id),
        "username": user.username,
        "role_id": user.role_id
    })

    return {
        "success": True,
        "message": "Login successfully",
        "data": {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role_id": user.role_id
            }
        }
    }