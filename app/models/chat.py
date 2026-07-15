from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from app.db.base import Base

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key = True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    last_message_at = Column(DateTime, server_default=func.now())