from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aircraft(Base):
    __tablename__ = 'aircraft'

    id = Column(Integer, primary_key=True, index=True)
    registration = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    last_maintenance = Column(Date, nullable=True)
    next_maintenance = Column(Date, nullable=True)
