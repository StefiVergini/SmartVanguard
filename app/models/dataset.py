from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from app.db.base import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    filename = Column(String)
    file_type = Column(String)
    rows_count = Column(Integer)
    columns_count = Column(Integer)
    status = Column(String(30), default="processing")
    created_at  = Column(DateTime, server_default=func.now())
    size_mb = Column(Float)
    dataset_type = Column(String(50))

#file_type si es csv, txt, etc
#dataset_type: tipos de datos que contiene el archivo como
#    sales
#    employees
#    payments
#    attendance
#    inventory
#    students



