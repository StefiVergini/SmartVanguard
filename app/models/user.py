from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True)
   email = Column(String(255), unique=True, nullable=False)
   password_hash = Column(String, nullable=False)
   company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
   full_name = Column(String(250))
   role = Column(String(30), default="user")
   created_at  = Column(DateTime, server_default=func.now())
   is_active = Column(Boolean, default=True) 

   company = relationship(
    "Company",
    back_populates="users"
   )
   uploaded_datasets = relationship(
    "Dataset",
    back_populates="uploaded_by_user"
   )

   chats = relationship(
    "Chat",
    back_populates="user"
   )
   ai_insights = relationship(
    "AIInsight",
    back_populates="user"
   )
   audit_logs = relationship(
    "AuditLog",
    back_populates="user"
   )
