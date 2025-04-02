from flask import Blueprint
from app.controllers.auth_controller import login, register

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/', methods=['GET', 'POST'])(login)
auth_bp.route('/register', methods=['GET', 'POST'])(register)
