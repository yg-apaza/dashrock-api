from sqlalchemy import Column, String, Integer, TIMESTAMP, Float
from app.database import Base


class Issue(Base):
    __tablename__ = 'issues'

    atm_id = Column('ATM_ID', String, primary_key=True, nullable=True)
    sitio = Column('SITIO', String)
    division = Column('division', String)
    tipo_sitio = Column('TIPO_SITIO', String)
    marca_modelo = Column('MARCA_MODELO', String)
    falla = Column('FALLA', String)
    fecha_inicio = Column('FECHA_INICIO', TIMESTAMP(timezone=False))
    fecha_fin = Column('FECHA_FIN', TIMESTAMP(timezone=False))
    duracion = Column('DURACION', Float)
    impacto = Column('IMPACTO', Integer)
    ticket_key = Column('TICKET_KEY', String)
    estado = Column('ESTADO', String)
    cr = Column('CR', Integer)
    autoservicio = Column('AUTOSERVICIO', String)
    name = Column('NAME', String)
    fault_id = Column('faultid', Integer)
    generacion = Column('generacion', String)
