from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Atm(BaseModel):
    latitud: Optional[float]
    longitud: Optional[float]
    sitio: Optional[str]
    calle: Optional[str]
    estado: Optional[str]
    ciudad: Optional[str]
    colonia: Optional[str]
    total_atms: int
    total_atms_falla: int

    class Config:
        orm_mode = True


class AtmRequest(BaseModel):
    latitud: float
    longitud: float
    fecha: datetime
    radio: Optional[float]

    class Config:
        orm_mode = True
