from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from base_mixins import SoftDeleteMixin
from timestamp_mixin import TimestampMixin

class PromptTemplate(SoftDeleteMixin,TimestampMixin, Base):

    __tablename__ = "prompt_templates"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String)
    business_type = Column(String)
    system_prompt = Column(Text)
    is_default = Column(Boolean, default=False)
    version = Column(Integer, default=1)

    company = relationship(
        "Company",
        back_populates="prompt_templates"
    )