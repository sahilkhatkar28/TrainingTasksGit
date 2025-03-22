from flask import Blueprint
from src.controllers.comment_controller import create_comment, get_comments

comment_bp = Blueprint('comment_bp', __name__)

comment_bp.route('/comments', methods=['POST'])(create_comment)
comment_bp.route('/posts/<int:post_id>/comments', methods=['GET'])(get_comments)
