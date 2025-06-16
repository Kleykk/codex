from sqlalchemy.orm import Session
from . import models, schemas


def get_aircraft(db: Session, aircraft_id: int):
    return db.query(models.Aircraft).filter(models.Aircraft.id == aircraft_id).first()


def get_aircrafts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Aircraft).offset(skip).limit(limit).all()


def create_aircraft(db: Session, aircraft: schemas.AircraftCreate):
    db_item = models.Aircraft(**aircraft.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
