from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from app.db.base import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key = True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now())