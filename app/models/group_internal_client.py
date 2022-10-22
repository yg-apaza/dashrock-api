from sqlalchemy import Column, String
from app.database import Base


class GroupInternalClient(Base):
    __tablename__ = 'group_internal_client'

    atm_id = Column('ID', String, primary_key=True, nullable=True)
    group = Column('Grupo', String)
