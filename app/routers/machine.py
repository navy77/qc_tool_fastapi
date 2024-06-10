from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Machine)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(database.get_db)):
    return crud.create_machine(db=db, machine=machine)

@router.get("/{machine_id}", response_model=schemas.Machine)
def read_machine(machine_id: int, db: Session = Depends(database.get_db)):
    db_machine = crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return db_machine

@router.get("/project/{project_id}", response_model=list[schemas.Machine])
def read_machines_by_project(project_id: int, db: Session = Depends(database.get_db)):
    machines = crud.get_machines_by_project(db, project_id=project_id)
    if not machines:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machines

@router.get("/", response_model=list[schemas.Machine])
def read_machines(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    machines = crud.get_all_machine(db, skip=skip, limit=limit)
    return machines


@router.put("/{machine_id}", response_model=schemas.Machine)
def update_machine(machine_id: int, machine: schemas.MachineCreate, db: Session = Depends(database.get_db)):
    db_machine = crud.update_machine(db, machine_id=machine_id, machine=machine)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return db_machine

@router.delete("/{machine_id}", response_model=schemas.Machine)
def delete_machine(machine_id: int, db: Session = Depends(database.get_db)):
    db_machine = crud.delete_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return db_machine