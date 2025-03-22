from flask import request, jsonify
from src.services.comment_service import CommentService

def create_comment():
    data = request.json
    return jsonify(CommentService.create_comment(data))

def get_comments(post_id):
    return jsonify(CommentService.get_comments(post_id))
