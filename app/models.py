from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Specification(Base):
    __tablename__ = "specification"
    spec_id = Column(String(50), primary_key=True, index=True)  # Defined length for VARCHAR
    model = Column(String(100))  # Defined length for VARCHAR
    spec = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    
    measurements = relationship("Measure", back_populates="spec_details")

class Measure(Base):
    __tablename__ = "measure"
    id = Column(Integer, primary_key=True, index=True)

    spec_id = Column(String(50), ForeignKey("specification.spec_id"), index=True)  # Defined length for VARCHAR
    measure_time = Column(DateTime)
    model = Column(String(100), index=True)  # Defined length for VARCHAR
    lot_no = Column(String(100))  # Defined length for VARCHAR
    machine_no = Column(String(100))  # Defined length for VARCHAR
    instrument_no = Column(String(100))  # Defined length for VARCHAR
    spec = Column(Float)
    spec_max = Column(Float)
    spec_min = Column(Float)
    value = Column(Float)
    judgment = Column(String(100))  # Defined length for VARCHAR
    employee = Column(String(100))  # Defined length for VARCHAR

    spec_details = relationship("Specification", back_populates="measurements")

class Calibration(Base):
    __tablename__ = "calibration"
    instrument_no = Column(String(50), primary_key=True, index=True)  # Defined length for VARCHAR
    instrument_name = Column(String(100))  # Defined length for VARCHAR
    exp_date = Column(DateTime)
    calibration_no = Column(String(100))  # Defined length for VARCHAR
