from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Atm(BaseModel):
    atm_id: Optional[str]
    latitud: Optional[float]
    longitud: Optional[float]
    status: bool = True
    sitio: Optional[str]
    calle: Optional[str]
    estado: Optional[str]
    ciudad: Optional[str]
    colonia: Optional[str]

    class Config:
        orm_mode = True


class AtmRequest(BaseModel):
    latitud: float
    longitud: float
    fecha: datetime
    radio: Optional[float]

    class Config:
        orm_mode = True
