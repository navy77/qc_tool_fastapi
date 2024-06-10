from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Status)
def create_status(status: schemas.StatusCreate, db: Session = Depends(database.get_db)):
    return crud.create_status(db=db, status=status)

@router.get("/{status_id}", response_model=schemas.Status)
def read_status(status_id: int, db: Session = Depends(database.get_db)):
    db_status = crud.get_status(db, status_id=status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status

@router.get("/project/{project_id}", response_model=list[schemas.Status])
def read_status_by_project(project_id: int, db: Session = Depends(database.get_db)):
    status = crud.get_status_by_project(db, project_id=project_id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@router.get("/", response_model=list[schemas.Status])
def read_statuses(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    statuses = crud.get_all_status(db, skip=skip, limit=limit)
    return statuses

@router.put("/{status_id}", response_model=schemas.Status)
def update_status(status_id: int, status: schemas.StatusCreate, db: Session = Depends(database.get_db)):
    db_status = crud.update_status(db, status_id=status_id, status=status)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status

@router.delete("/{status_id}", response_model=schemas.Status)
def delete_status(status_id: int, db: Session = Depends(database.get_db)):
    db_status = crud.delete_status(db, status_id=status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status