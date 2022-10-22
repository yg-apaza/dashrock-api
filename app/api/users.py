from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user
