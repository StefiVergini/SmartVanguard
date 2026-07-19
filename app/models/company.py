from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    business_type = Column(String(50), nullable=False)

    created_at = Column(DateTime, server_default=func.now())

    is_active = Column(Boolean, default=True)

    plan = Column(String(30), nullable=False, default="starter")

    max_users = Column(Integer, default=5)

    max_storage = Column(Float, default=2.0)

    max_datasets = Column(Integer, default=20)

    users = relationship(
        "User",
        back_populates="company"
    )

    datasets = relationship(
        "Dataset",
        back_populates="company"
    )

    employees = relationship(
        "Employee",
        back_populates="company"
    )

    chats = relationship(
        "Chat",
        back_populates="company"
    )

    ai_insights = relationship(
        "AIInsight",
        back_populates="company"
    )
    audit_logs = relationship(
        "AuditLog",
        back_populates="company"
    )
    prompt_templates = relationship(
        "PromptTemplate",
        back_populates="company"
    )
