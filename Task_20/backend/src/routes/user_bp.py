from flask import Blueprint
from src.controller.user_controller import signin , register

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/register',methods = ['POST'])(register)
user_bp.route('/signin',methods = ['POST'])(signin)  