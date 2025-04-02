from flask import request, Response, json, jsonify
from src.services import comment_service

def add_comment():
    data = request.json
    response, status = comment_service.add_comment(data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

def get_comments(post_id):
    response, status = comment_service.get_comments(post_id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

def delete_comment(comment_id):
    data = request.json
    response, status = comment_service.delete_comment(comment_id, data.get('user_id'))
    return Response(response=json.dumps(response), status=status, mimetype='application/json')
