from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Boolean
from app.db.base import Base

class PromptTemplate(Base):

    __tablename__ = "prompt_templates"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    name = Column(String)
    business_type = Column(String)
    system_prompt = Column(Text)
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())