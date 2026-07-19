from sqlalchemy import (
    Column,
    Integer,
    Text,
    Float,
    DateTime,
    ForeignKey,
    func,
    String
)
from sqlalchemy.orm import relationship

from app.db.base import Base

#Telemetría de la IA

class AIInsight(Base):

    __tablename__ = "ai_insights"

    id = Column(Integer, primary_key=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    chat_id = Column(
        Integer,
        ForeignKey("chats.id"),
        nullable=False
    )
    chat_message_id = Column(
        Integer,
        ForeignKey("chat_messages.id")
    )
    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    tokens_used = Column(Integer)

    processing_time = Column(Float)
    
    model_used = Column(String(100))

    cost = Column(Float)
    status = Column(
        String(30),
        default="completed"
    ) #processing, completed, failed, cancelled
   
    provider = Column(String(50))

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    company = relationship(
        "Company",
        back_populates= "ai_insights"
    )
    user = relationship(
        "User",
        back_populates="ai_insights"
    )
    chat = relationship(
        "Chat",
        back_populates="ai_insights"
    )
    chat_message = relationship(
        "ChatMessage",
        back_populates="ai_insight"
    )