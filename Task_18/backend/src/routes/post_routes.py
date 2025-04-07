from flask import Blueprint
from src.controller.post_controller import create , get_all

post_bp = Blueprint("post_bp",__name__)

post_bp.route('/create_post',methods=['POST'])(create)
post_bp.route('/get_post',methods=['GET'])(get_all)