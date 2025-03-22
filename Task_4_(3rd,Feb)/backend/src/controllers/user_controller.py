from flask import request ,Response,json ,jsonify,g
from src.services import user_role_service

def signup():
    data=request.json
    response,status= user_role_service.signup(data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')

def login():
    data =request.json
    response,status = user_role_service.login(data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')
