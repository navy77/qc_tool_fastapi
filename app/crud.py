from sqlalchemy.orm import Session
from . import schemas,models
######  project  ########

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.project_id == project_id).first()

def get_all_project(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if db_project:
        db_project.project_name = project.project_name
        db_project.process_name = project.process_name
        db.commit()
        db.refresh(db_project)
        return db_project
    return None

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return db_project
    return None

######  data  ########
def create_data(db: Session, data: schemas.DataCreate):
    db_data = models.Data(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_data(db: Session, data_id: int):
    return db.query(models.Data).filter(models.Data.id == data_id).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Data).offset(skip).limit(limit).all()

def get_data_by_project(db: Session, project_id: int):
    return db.query(models.Data).filter(models.Data.project_id == project_id).all()


def update_data(db: Session, data_id: int, data: schemas.DataCreate):
    db_data = db.query(models.Data).filter(models.Data.id == data_id).first()
    if db_data:
        db_data.data_name = data.data_name
        db.commit()
        db.refresh(db_data)
        return db_data
    return None

def delete_data(db: Session, data_id: int):
    db_data = db.query(models.Data).filter(models.Data.id == data_id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
        return db_data
    return None

######  status  ########
def create_status(db: Session, status: schemas.StatusCreate):
    db_status = models.Status(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_status(db: Session, status_id: int):
    return db.query(models.Status).filter(models.Status.id == status_id).first()

def get_status_by_project(db: Session, project_id: int):
    return db.query(models.Status).filter(models.Status.project_id == project_id).all()

def get_all_status(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Status).offset(skip).limit(limit).all()

def update_status(db: Session, status_id: int, status: schemas.StatusCreate):
    db_status = db.query(models.Status).filter(models.Status.id == status_id).first()
    if db_status:
        db_status.status_name = status.status_name
        db.commit()
        db.refresh(db_status)
        return db_status
    return None

def delete_status(db: Session, status_id: int):
    db_status = db.query(models.Status).filter(models.Status.id == status_id).first()
    if db_status:
        db.delete(db_status)
        db.commit()
        return db_status
    return None

######  alarm  ########
def create_alarm(db: Session, alarm: schemas.AlarmCreate):
    db_alarm = models.Alarm(**alarm.dict())
    db.add(db_alarm)
    db.commit()
    db.refresh(db_alarm)
    return db_alarm

def get_alarm(db: Session, alarm_id: int):
    return db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()

def get_alarms_by_project(db: Session, project_id: int):
    return db.query(models.Alarm).filter(models.Alarm.project_id == project_id).all()

def get_all_alarm(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Alarm).offset(skip).limit(limit).all()

def update_alarm(db: Session, alarm_id: int, alarm: schemas.AlarmCreate):
    db_alarm = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    if db_alarm:
        db_alarm.alarm_name = alarm.alarm_name
        db.commit()
        db.refresh(db_alarm)
        return db_alarm
    return None

def delete_alarm(db: Session, alarm_id: int):
    db_alarm = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    if db_alarm:
        db.delete(db_alarm)
        db.commit()
        return db_alarm
    return None

######  machine  ########
def create_machine(db: Session, machine: schemas.MachineCreate):
    db_machine = models.Machine(**machine.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine

def get_machine(db: Session, machine_id: int):
    return db.query(models.Machine).filter(models.Machine.id == machine_id).first()

def get_machines_by_project(db: Session, project_id: int):
    return db.query(models.Machine).filter(models.Machine.project_id == project_id).all()

def get_all_machine(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Machine).offset(skip).limit(limit).all()

def update_machine(db: Session, machine_id: int, machine: schemas.MachineCreate):
    db_machine = db.query(models.Machine).filter(models.Machine.id == machine_id).first()
    if db_machine:
        db_machine.machine_name = machine.machine_name
        db.commit()
        db.refresh(db_machine)
        return db_machine
    return None

def delete_machine(db: Session, machine_id: int):
    db_machine = db.query(models.Machine).filter(models.Machine.id == machine_id).first()
    if db_machine:
        db.delete(db_machine)
        db.commit()
        return db_machine
    return None