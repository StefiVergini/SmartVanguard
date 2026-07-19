from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    employee_code = Column(String(30), unique=True)
    full_name = Column(String)
    department = Column(String)
    position = Column(String)
    status = Column(String(30), default="active")
    hire_date = Column(DateTime)
    termination_date = Column(DateTime)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(30))
    company = relationship(
        "Company",
        back_populates="employees"
    )