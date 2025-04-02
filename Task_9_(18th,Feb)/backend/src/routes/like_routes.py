from flask import Blueprint
from src.controllers.like_controller import like_post, unlike_post

like_bp = Blueprint('like_bp', __name__)

like_bp.route('/like', methods=['POST'])(like_post)
like_bp.route('/unlike', methods=['POST'])(unlike_post)
