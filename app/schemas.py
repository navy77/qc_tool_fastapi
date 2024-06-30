from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SpecificationBase(BaseModel):
    spec_id: str
    model: str
    spec: float 
    spec_max: float
    spec_min: float

class SpecificationCreate(SpecificationBase):
    pass

class Specification(SpecificationBase):
    spec_id: str

    class Config:
        from_attributes = True

class MeasureBase(BaseModel):
    measure_time: datetime
    model: str
    lot_no: str
    machine_no: str
    instrument_no: str
    value: float
    spec: float
    spec_max: float
    spec_min: float
    judgment: str
    employee: str
    

class MeasureCreate(MeasureBase):
    spec_id: str

class Measure(MeasureBase):
    id: int
    spec_id: str

    class Config:
        from_attributes = True

class CalibrationBase(BaseModel):
    instrument_name: str
    exp_date: datetime
    calibration_no: str

class CalibrationCreate(CalibrationBase):
    instrument_no: str

class Calibration(CalibrationBase):
    instrument_no: Optional[str] = None

    class Config:
        from_attributes = True
