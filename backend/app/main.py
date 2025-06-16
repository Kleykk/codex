from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/aircraft/", response_model=schemas.Aircraft)
def create_aircraft(aircraft: schemas.AircraftCreate, db: Session = Depends(get_db)):
    return crud.create_aircraft(db=db, aircraft=aircraft)

@app.get("/aircraft/", response_model=list[schemas.Aircraft])
def read_aircrafts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_aircrafts(db, skip=skip, limit=limit)
    return items

@app.get("/aircraft/{aircraft_id}", response_model=schemas.Aircraft)
def read_aircraft(aircraft_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_aircraft(db, aircraft_id=aircraft_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Aircraft not found")
    return db_item
