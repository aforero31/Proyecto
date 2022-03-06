from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Competidor(Base):
    __tablename__ = 'competidor'

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(200),nullable=False,unique=True)
    Probabilidad = Column(Float)
    carrera = Column(Integer, ForeignKey('carrera.id'))
    Apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')