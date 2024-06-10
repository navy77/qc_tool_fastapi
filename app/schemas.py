from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SpecificationBase(BaseModel):
    model: str
    spec: float 
    spec_max: float
    spec_min: float

class SpecificationCreate(SpecificationBase):
    pass

class Specification(SpecificationBase):
    spec_id: str

    class Config:
        from_attributes  = True


class Measure_dataBase(BaseModel):
    measure_time: datetime
    model:str
    lot_no = str
    machine_no = str
    instrument_no = str
    value = float
    spec_nom = float
    spec_max = float
    spec_min = float
    judgment = str
    employee = str

class Measure_dataCreate(Measure_dataBase):
    spec_id: str

class Measure_data(Measure_dataBase):
    id: int
    spec_id: str

    class Config:
        from_attributes  = True

class CalibrationBase(BaseModel):
    instrument_no: str
    instrument_name:str
    exp_date:datetime
    calibration_no:str

class CalibrationCreate(CalibrationBase):
    pass

class Calibration(CalibrationBase):
    pass

    class Config:
        from_attributes  = True



