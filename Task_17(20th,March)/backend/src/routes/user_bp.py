from flask import Blueprint
from src.controlers.user_controls import signup ,login

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/signup',methods=['POST'])(signup)
user_bp.route('/login',methods=['POST'])(login) 