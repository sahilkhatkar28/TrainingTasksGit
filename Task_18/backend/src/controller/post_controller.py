from flask import request , jsonify
from src.services.post_service import PostService
from flask_jwt_extended import jwt_required

@jwt_required()
def create():
    data = request.json
    return jsonify(PostService.create_post(data))

@jwt_required()
def get_all():
    return jsonify(PostService.get_all_posts())