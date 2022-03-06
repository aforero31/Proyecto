from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from .declarative_base import Base

class Apostador(Base):
    __tablename__='apostador'

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(200),nullable=False,unique=True)
    Apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')