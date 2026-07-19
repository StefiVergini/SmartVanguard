from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key = True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    last_message_at = Column(DateTime, server_default=func.now())
    company = relationship(
        "Company",
        back_populates="chats"
    )

    user = relationship(
        "User",
        back_populates="chats"
    )

    messages = relationship(
        "ChatMessage",
        back_populates="chat",
        cascade="all, delete-orphan"
    )

    ai_insights = relationship(
        "AIInsight",
        back_populates="chat"
    )