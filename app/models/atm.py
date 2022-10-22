from sqlalchemy import Column, String, Integer, TIMESTAMP, Float
from app.database import Base


class Atm(Base):
    __tablename__ = 'atms'

    atm_id = Column('ATM', String, primary_key=True, nullable=True)
    sitio = Column('Sitio', String)
    cr = Column('CR', Integer)
    division = Column('Division', String)
    marca = Column('Marca', String)
    tipo_dispositivo = Column('Tipo_dispositivo', String)
    estatus_dispositivo = Column('Estatus_dispositivo', String)
    calle = Column('Calle', String)
    num_ext = Column('Num__Ext_', String)
    estado = Column('Estado', String)
    ciudad = Column('Ciudad', String)
    cp = Column('CP', String)
    del_muni = Column('Del_Muni', String)
    colonia = Column('Colonia', String)
    latitud = Column('Latitud', Float)
    longitud = Column('Longitud', Float)
    tipo_localidad = Column('Tipo_localidad', String)
    idc = Column('IDC', String)
    etv = Column('ETV', String)
