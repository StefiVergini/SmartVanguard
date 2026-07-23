from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from timestamp_mixin import TimestampMixin

class ChatMessage(TimestampMixin, Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key = True)
    chat_id = Column(Integer, ForeignKey("chats.id"), nullable=False)
    role = Column(String)
    content = Column(Text)
   
    chat = relationship(
        "Chat",
        back_populates="messages"
    )
    ai_insight = relationship(
        "AIInsight",
        back_populates="chat_message",
        uselist=False
    )