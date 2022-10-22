from sqlalchemy import Column, Boolean, String, Integer
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(512))
    email = Column(String(512), unique=True, nullable=False)
    hashed_password = Column(String(60), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    is_internal_client = Column(Boolean())
    group = Column(String)
