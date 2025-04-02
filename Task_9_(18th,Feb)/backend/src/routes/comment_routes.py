from flask import Blueprint
from src.controllers.comment_controller import add_comment, get_comments, delete_comment

comment_bp = Blueprint('comment_bp', __name__)

comment_bp.route('/add', methods=['POST'])(add_comment)
comment_bp.route('/<post_id>', methods=['GET'])(get_comments)
comment_bp.route('/delete/<comment_id>', methods=['DELETE'])(delete_comment)
