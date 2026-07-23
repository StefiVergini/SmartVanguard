from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from timestamp_mixin import TimestampMixin
from base_mixins import SoftDeleteMixin

class User(TimestampMixin, SoftDeleteMixin, Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True)
   email = Column(String(255), unique=True, nullable=False)
   password_hash = Column(String, nullable=False)
   company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
   full_name = Column(String(250))
   role = Column(String(30), default="user")

   company = relationship(
    "Company",
    back_populates="users"
   )
   uploaded_datasets = relationship(
    "Dataset",
    back_populates="uploaded_by_user",
    lazy="selectin"
   )

   chats = relationship(
    "Chat",
    back_populates="user",
    lazy="selectin"
   )
   ai_insights = relationship(
    "AIInsight",
    back_populates="user",
    lazy="selectin"
   )
   audit_logs = relationship(
    "AuditLog",
    back_populates="user",
    lazy="selectin"
   )
