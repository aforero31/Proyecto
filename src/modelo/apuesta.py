from sqlalchemy import Column, ForeignKey, Integer
from .declarative_base import Base

class Apuesta(Base):
    __tablename__ = 'apuesta'

    id = Column(Integer, primary_key=True)
    Carrera = Column(Integer, ForeignKey('carrera.id'))
    Competidor = Column(Integer, ForeignKey('competidor.id'))
    Apostador = Column(Integer, ForeignKey('apostador.id'))
    Valor = Column(Integer)