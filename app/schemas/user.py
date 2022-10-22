from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None
    is_internal_client: bool
    group: Optional[str] = None

    class Config:
        orm_mode = True
