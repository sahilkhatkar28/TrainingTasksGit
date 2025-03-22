from flask import request, jsonify
from src.services.user_service import UserService

def signup():
    data = request.json
    return jsonify(UserService.signup(data))

def login():
    data = request.json
    return jsonify(UserService.login(data))
