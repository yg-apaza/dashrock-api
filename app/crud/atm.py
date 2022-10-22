from typing import List
from sqlalchemy.orm import Session

from app.models.atm import Atm


def get_all(db: Session, radio: float) -> List[Atm]:
    return db.query(Atm).filter(
        Atm.ciudad == 'CIUDAD DE MEXICO', Atm.colonia == 'SAN ANGEL'
    ).all()
