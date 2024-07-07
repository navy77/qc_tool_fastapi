from sqlalchemy import Column, Integer, String, ForeignKey,Float,DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Specification(Base):
    __tablename__ = "specification_db"
    spec_id = Column(String(5), primary_key=True, index=True)
    spec_name = Column(String(10))
    model = Column(String(10))
    spec = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    point = Column(Integer)
    method = Column(Integer)

class Measure(Base):
    __tablename__ = "measure_db"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    spec_id = Column(String(5))
    spec_name = Column(String(10))
    measure_time = Column(DateTime)
    model = Column(String(10))
    lot_no = Column(String(10))
    machine_no = Column(String(10))
    instrument_no = Column(String(10))
    spec = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    point = Column(Integer)
    value = Column(Float)
    judgment = Column(String(2))
    employee_no = Column(String(5))

class Calibration(Base):
    __tablename__ = "carlibration_db"
    instrument_no = Column(String(10), primary_key=True, index=True)
    instrument_name = Column(String)
    exp_date = Column(DateTime)
    calibration_no = Column(String)

class User(Base):
    __tablename__ = "user_tb"
    email = Column(String(30), primary_key=True, index=True)
    password = Column(String)
    role = Column(Integer)