from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Data)
def create_data(data: schemas.DataCreate, db: Session = Depends(database.get_db)):
    return crud.create_data(db=db, data=data)

@router.get("/{data_id}", response_model=schemas.Data)
def read_data(data_id: int, db: Session = Depends(database.get_db)):
    db_data = crud.get_data(db, data_id=data_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data

@router.get("/project/{project_id}", response_model=list[schemas.Data])
def read_data_by_project(project_id: int, db: Session = Depends(database.get_db)):
    data = crud.get_data_by_project(db, project_id=project_id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.get("/", response_model=list[schemas.Data])
def read_datas(limit: int = 10, db: Session = Depends(database.get_db)):
    datas = crud.get_all_data(db,  limit=limit)
    return datas


@router.put("/{data_id}", response_model=schemas.Data)
def update_data(data_id: int, data: schemas.DataCreate, db: Session = Depends(database.get_db)):
    db_data = crud.update_data(db, data_id=data_id, data=data)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data

@router.delete("/{data_id}", response_model=schemas.Data)
def delete_data(data_id: int, db: Session = Depends(database.get_db)):
    db_data = crud.delete_data(db, data_id=data_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data