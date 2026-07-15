from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, Float
from app.db.base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    business_type = Column(String(50), nullable=False)
    created_at  = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True) 
    plan = Column(String(30), nullable=False, default="starter")
    max_users = Column(Integer, default=5)
    max_storage = Column(Float, default=2.0)
    max_datasets = Column(Integer, default=20)

    






