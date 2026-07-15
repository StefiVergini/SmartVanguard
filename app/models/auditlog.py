from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from app.db.base import Base

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    entity = Column(String)
    entity_id = Column(Integer)
    description = Column(Text)
    ip_address = Column(String)
    created_at = Column(DateTime, server_default=func.now())