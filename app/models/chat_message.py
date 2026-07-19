from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key = True)
    chat_id = Column(Integer, ForeignKey("chats.id"), nullable=False)
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
   
    chat = relationship(
        "Chat",
        back_populates="messages"
    )
    ai_insight = relationship(
        "AIInsight",
        back_populates="chat_message",
        uselist=False
    )