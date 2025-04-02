from app.models.message_model import Message
from app.models import db

class ChatService:
    @staticmethod
    def save_message(room, sender, message):
        msg = Message(room=room, sender=sender, message=message)
        db.session.add(msg)
        db.session.commit()

    @staticmethod
    def get_chat_history(room):
        return Message.query.filter_by(room=room).order_by(Message.timestamp.asc()).all()
