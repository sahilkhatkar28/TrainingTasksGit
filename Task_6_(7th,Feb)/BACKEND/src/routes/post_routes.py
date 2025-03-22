from flask import Blueprint
from src.controllers.post_controller import create_post, get_posts

post_bp = Blueprint('post_bp', __name__)

post_bp.route('/posts', methods=['POST'])(create_post)
post_bp.route('/posts', methods=['GET'])(get_posts)
