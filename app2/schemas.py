from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SpecificationBase(BaseModel):
    spec_id:str
    spec_name :str
    model: str
    spec: float 
    spec_max: float
    spec_min: float
    point: int
    method: int

class SpecificationCreate(SpecificationBase):
    pass

class Specification(SpecificationBase):
    spec_id: str

    class Config:
        from_attributes  = True


class MeasureBase(BaseModel):
    spec_id: str
    spec_name:str
    measure_time: datetime
    model:str
    lot_no:str
    machine_no: str
    instrument_no: str
    spec: float
    spec_max:float
    spec_min:float
    point:int
    value:float
    judgment: str
    employee_no :str

class MeasureCreate(MeasureBase):
    pass

class Measure(MeasureBase):
    # id: int
    pass

    class Config:
        from_attributes  = True

class CalibrationBase(BaseModel):
    instrument_no:str
    instrument_name:str
    exp_date:datetime
    calibration_no:str

class CalibrationCreate(CalibrationBase):
    pass

class Calibration(CalibrationBase):
    instrument_no:str

    class Config:
        from_attributes  = True


class UserBase(BaseModel):
    password:str
    role:int=2

class UserCreate(UserBase):
    pass

class User(UserBase):
    email:str

    class Config:
        from_attributes  = True
