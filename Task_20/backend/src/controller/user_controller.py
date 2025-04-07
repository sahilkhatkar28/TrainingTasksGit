from flask import request , jsonify
from src.services.user_services import UserService

def register():
    data = request.json
    return jsonify(UserService.signup(data))

def signin():
    data = request.json
    return jsonify(UserService.login(data))
