from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class PromptTemplate(Base):

    __tablename__ = "prompt_templates"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String)
    business_type = Column(String)
    system_prompt = Column(Text)
    is_default = Column(Boolean, default=False)
    version = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    company = relationship(
        "Company",
        back_populates="prompt_templates"
    )