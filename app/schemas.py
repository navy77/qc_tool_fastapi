from pydantic import BaseModel
from typing import List, Optional


class SpecificationBase(BaseModel):
    project_name: str
    divison_name: str 
    process_name: str
    
class ProjectCreate(SpecificationBase):
    pass

class Project(ProjectBase):
    project_id: int

    class Config:
        from_attributes  = True


class DataBase(BaseModel):
    data_name: str

class DataCreate(DataBase):
    project_id: int

class Data(DataBase):
    id: int
    project_id: int

    class Config:
        from_attributes  = True


class StatusBase(BaseModel):
    status_name: str

class StatusCreate(StatusBase):
    project_id: int

class Status(StatusBase):
    id: int
    project_id: int

    class Config:
        from_attributes  = True


class AlarmBase(BaseModel):
    alarm_name: str

class AlarmCreate(AlarmBase):
    project_id: int

class Alarm(AlarmBase):
    id: int
    project_id: int

    class Config:
        from_attributes  = True


class MachineBase(BaseModel):
    machine_name: str

class MachineCreate(MachineBase):
    project_id: int

class Machine(MachineBase):
    id: int
    project_id: int

    class Config:
        from_attributes  = True

