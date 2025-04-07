from src.services.comment_service import CommentService
from flask import jsonify , request
from flask_jwt_extended import jwt_required

@jwt_required()
def create_c():
    data = request.json
    return jsonify(CommentService.create_comment(data))

@jwt_required()
def get_c(post_name):
    return jsonify(CommentService.get_comments(post_name))