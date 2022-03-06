from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Carrera(Base):
    __tablename__='carrera'

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(200),nullable=False,unique=True)
    Abierta = Column(Boolean)
    Competidores = relationship('Competidor', cascade='all, delete, delete-orphan')
    Apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')

