from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.repositories.base_repository import BaseRepository

class ChatRepository(BaseRepository[Chat]):
    
    def __init__(self):
        super().__init__(Chat)

    def get_user_chats(self, db: Session, user_id: int):
       
        return (
            db.query(Chat)
            .filter(Chat.user_id == user_id)
            .order_by(Chat.last_message_at.desc())
            .all()
        )


    def rename_chat( self, db: Session, chat_id: int, new_title: str):

        chat = self.get_by_id(db, chat_id)

        if chat is None:
            return None

        return self.update(
            db,
            chat,
            title=new_title
        )
