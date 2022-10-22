from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.api import deps
from app.schemas.atm import AtmRequest
from app import crud


router = APIRouter()


@router.post("/nearby", response_model=List[schemas.Atm])
def get_nearby_atms(
    request: AtmRequest,
    db: Session = Depends(deps.get_db)
) -> Any:
    return crud.atm.get_nearby(
        db, request.latitud, request.longitud, request.radio, request.fecha
    )
