from flask import request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services import post_service

@jwt_required()
def create_post():
    data = request.json
    user_id = get_jwt_identity()  # Extract user_id from JWT
    response, status = post_service.create_post(data, user_id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def get_all_posts():
    response, status = post_service.get_all_posts()
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def delete_post(post_id):
    user_id = get_jwt_identity()  # Extract user_id from JWT
    response, status = post_service.delete_post(post_id, user_id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')
