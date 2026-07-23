from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship
from app.db.base import Base
from base_mixins import SoftDeleteMixin
from timestamp_mixin import TimestampMixin

class Chat(SoftDeleteMixin, TimestampMixin, Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key = True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String)
    last_message_at = Column(DateTime, server_default=func.now())
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime)
    deleted_by = Column(Integer, ForeignKey("users.id"))

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
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    ai_insights = relationship(
        "AIInsight",
        back_populates="chat",
        lazy="selectin"
    )

Index("idx_chat_company", Chat.company_id)