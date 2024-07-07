from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Measure)
def create_measure(measure: schemas.MeasureCreate, db: Session = Depends(database.get_db)):
    return crud.create_measure(db=db, measure=measure)


@router.get("/", response_model=list[schemas.Measure])
def read_measures(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    measures = crud.get_all_measure(db, skip=skip, limit=limit)
    return measures

@router.get("/spec/{spec_id}", response_model=list[schemas.Measure])
def read_measure_by_spec_id(spec_id: str, db: Session = Depends(database.get_db)):
    measure = crud.get_measure_by_spec_id(db, spec_id=spec_id)
    if not measure:
        raise HTTPException(status_code=404, detail="Measure not found")
    return measure

@router.get("/model/{model}", response_model=list[schemas.Measure])
def read_measure_by_model(model: str, db: Session = Depends(database.get_db)):
    measure = crud.get_measure_by_model(db, model=model)
    if not measure:
        raise HTTPException(status_code=404, detail="Measure not found")
    return measure

@router.get("/lot_no/{lot_no}", response_model=list[schemas.Measure])
def read_measure_by_lot_no(lot_no: str, db: Session = Depends(database.get_db)):
    measure = crud.get_measure_by_lot_no(db, lot_no=lot_no)
    if not measure:
        raise HTTPException(status_code=404, detail="Measure not found")
    return measure

@router.get("/machine_no/{machine_no}", response_model=list[schemas.Measure])
def read_measure_by_machine_no(machine_no: str, db: Session = Depends(database.get_db)):
    measure = crud.get_measure_by_machine_no(db, machine_no=machine_no)
    if not measure:
        raise HTTPException(status_code=404, detail="Measure not found")
    return measure

@router.get("/instrument_no/{instrument_no}", response_model=list[schemas.Measure])
def read_measure_by_instrument_no(instrument_no: str, db: Session = Depends(database.get_db)):
    measure = crud.get_measure_by_instrument_no(db, instrument_no=instrument_no)
    if not measure:
        raise HTTPException(status_code=404, detail="Measure not found")
    return measure

@router.put("/{id}", response_model=schemas.Measure)
def update_measure(id: int, measure: schemas.MeasureCreate, db: Session = Depends(database.get_db)):
    db_measure = crud.update_measure(db, id=id, measure=measure)
    if db_measure is None:
        raise HTTPException(status_code=404, detail="Measure not found")
    return db_measure

@router.delete("/{id}", response_model=schemas.Measure)
def delete_measure(id: int, db: Session = Depends(database.get_db)):
    db_measure = crud.delete_measure(db, id=id)
    if db_measure is None:
        raise HTTPException(status_code=404, detail="Measure not found")
    return db_measure