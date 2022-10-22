from typing import Optional, Any

from sqlalchemy.orm import Session

from app.security import verify_password
from app.models.user import User


def get(db: Session, id: Any) -> Optional[User]:
    return db.query(User).filter(User.id == id).first()


def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def authenticate(db: Session, email: str, password: str) -> Optional[User]:
    user = get_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def is_active(user: User) -> bool:
    return user.is_active


def is_superuser(user: User) -> bool:
    return user.is_superuser
