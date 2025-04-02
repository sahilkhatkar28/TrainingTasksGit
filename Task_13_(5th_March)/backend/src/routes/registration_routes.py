from flask import Blueprint
from src.controller.registration_controller import register_user

user_bp = Blueprint("user_bp",__name__)

user_bp.route('/register',methods = ['POST'])(register_user)