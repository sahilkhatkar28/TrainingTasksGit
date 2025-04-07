from flask import Blueprint
from src.controller.comment_controller import create_c,get_c

comment_bp = Blueprint('comment_bp',__name__)

comment_bp.route("/create_c",methods = ["POST"])(create_c)
comment_bp.route("/get_c/<string:post_name>",methods = ["GET"])(get_c)  