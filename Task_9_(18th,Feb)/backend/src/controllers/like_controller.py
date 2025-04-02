from flask import request, Response, json, jsonify
from src.services import like_service

def like_post():
    data = request.json
    response, status = like_service.like_post(data.get('post_id'), data.get('user_id'))
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

def unlike_post():
    data = request.json
    response, status = like_service.unlike_post(data.get('post_id'), data.get('user_id'))
    return Response(response=json.dumps(response), status=status, mimetype='application/json')
