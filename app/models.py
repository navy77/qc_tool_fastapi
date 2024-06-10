from sqlalchemy import Column, Integer, String, ForeignKey,Float,DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Specification(Base):
    __tablename__ = "specification_db"
    spec_id = Column(String, primary_key=True, index=True)
    model = Column(String)
    spec = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    
    measurements = relationship("Measure_data", back_populates="spec_details")

class Measure_data(Base):
    __tablename__ = "measure_db"
    id = Column(Integer, primary_key=True, index=True)
    spec_id = Column(String, ForeignKey("specification_db.spec_id"),index=True)
    measure_time = Column(DateTime)
    model = Column(String, index=True)
    lot_no = Column(String)
    machine_no = Column(String)
    instrument_no = Column(String)
    value = Column(Float)
    spec_nom = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    judgment = Column(String)
    employee = Column(String)

    spec_details = relationship("Specification", back_populates="measurements")

class Calibration(Base):
    __tablename__ = "carlibration_db"
    id = Column(Integer, primary_key=True, index=True)
    instrument_no = Column(String,index=True)
    instrument_name = Column(String)
    exp_date = Column(DateTime)
    calibration_no = Column(String)