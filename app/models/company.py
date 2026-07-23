from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base import Base
from timestamp_mixin import TimestampMixin
from base_mixins import SoftDeleteMixin


class Company(TimestampMixin, SoftDeleteMixin, Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    business_type = Column(String(50), nullable=False)

    plan = Column(String(30), nullable=False, default="starter")

    max_users = Column(Integer, default=5)

    max_storage = Column(Float, default=2.0)

    max_datasets = Column(Integer, default=20)

    users = relationship(
        "User",
        back_populates="company",
        lazy="selectin"
    )

    datasets = relationship(
        "Dataset",
        back_populates="company",
        lazy="selectin"
    )

    employees = relationship(
        "Employee",
        back_populates="company",
        lazy="selectin"
    )

    chats = relationship(
        "Chat",
        back_populates="company",
        lazy="selectin"
    )

    ai_insights = relationship(
        "AIInsight",
        back_populates="company",
        lazy="selectin"
    )
    audit_logs = relationship(
        "AuditLog",
        back_populates="company",
        lazy="selectin"
    )
    prompt_templates = relationship(
        "PromptTemplate",
        back_populates="company",
        lazy="selectin"
    )
