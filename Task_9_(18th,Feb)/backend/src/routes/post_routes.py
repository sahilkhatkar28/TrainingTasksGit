from flask import Blueprint
from src.controllers.post_controller import create_post, get_all_posts, delete_post

post_bp = Blueprint('post_bp', __name__)

post_bp.route('/create', methods=['POST'])(create_post)
post_bp.route('/all', methods=['GET'])(get_all_posts)
post_bp.route('/delete/<post_id>', methods=['DELETE'])(delete_post)
