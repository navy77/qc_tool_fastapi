from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Alarm)
def create_alarm(alarm: schemas.AlarmCreate, db: Session = Depends(database.get_db)):
    return crud.create_alarm(db=db, alarm=alarm)

@router.get("/{alarm_id}", response_model=schemas.Alarm)
def read_alarm(alarm_id: int, db: Session = Depends(database.get_db)):
    db_alarm = crud.get_alarm(db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return db_alarm

@router.get("/project/{project_id}", response_model=list[schemas.Alarm])
def read_alarms_by_project(project_id: int, db: Session = Depends(database.get_db)):
    alarms = crud.get_alarms_by_project(db, project_id=project_id)
    if not alarms:
        raise HTTPException(status_code=404, detail="Alarms not found")
    return alarms

@router.get("/", response_model=list[schemas.Alarm])
def read_alarms(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    alarms = crud.get_all_alarm(db, skip=skip, limit=limit)
    return alarms

@router.put("/{alarm_id}", response_model=schemas.Alarm)
def update_alarm(alarm_id: int, alarm: schemas.AlarmCreate, db: Session = Depends(database.get_db)):
    db_alarm = crud.update_alarm(db, alarm_id=alarm_id, alarm=alarm)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_alarm

@router.delete("/{alarm_id}", response_model=schemas.Alarm)
def delete_alarm(alarm_id: int, db: Session = Depends(database.get_db)):
    db_alarm = crud.delete_alarm(db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return db_alarm