from flask import request, jsonify
from src.services.post_service import PostService

def create_post():
    data = request.json
    return jsonify(PostService.create_post(data))

def get_posts():
    return jsonify(PostService.get_all_posts())
