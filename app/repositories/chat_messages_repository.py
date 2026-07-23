from sqlalchemy.orm import Session

from app.models.chat_message import ChatMessage
from app.repositories.base_repository import BaseRepository

class ChatRepository(BaseRepository[ChatMessage]):
    
    def __init__(self):
        super().__init__(ChatMessage)    
        
    def get_chat_messages(self, db: Session, chat_id: int):
        
            return (
                db.query(ChatMessage)
                .filter(ChatMessage.chat_id == chat_id)
                .order_by(ChatMessage.created_at)
                .all()
            )
