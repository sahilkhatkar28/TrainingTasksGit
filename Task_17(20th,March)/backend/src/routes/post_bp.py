from flask import Blueprint
from src.controlers.blog_controls import createpost, updatepost, deletepost, getposts

post_bp = Blueprint('post_bp', __name__)

post_bp.add_url_rule('/createpost', view_func=createpost, methods=['POST'], endpoint="create_post")
post_bp.add_url_rule('/updatepost/<string:post_id>', view_func=updatepost, methods=['PUT'], endpoint="update_post")
post_bp.add_url_rule('/deletepost/<string:post_id>', view_func=deletepost, methods=['DELETE'], endpoint="delete_post")
post_bp.add_url_rule('/getposts', view_func=getposts, methods=['GET'], endpoint="get_posts")
