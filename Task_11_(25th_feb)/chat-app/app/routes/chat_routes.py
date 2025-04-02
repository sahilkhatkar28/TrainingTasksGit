from flask import Blueprint
from app.controllers.chat_controller import chat

chat_bp = Blueprint('chat', __name__)

chat_bp.route('/chat')(chat)
