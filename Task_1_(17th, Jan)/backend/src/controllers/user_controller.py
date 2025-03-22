from flask import request ,Response,json ,jsonify,g
from src.services import user_role_services

def signup():
    data=request.json
    response,status= user_role_services.signup(data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')

def login():
    data =request.json
    response,status = user_role_services.login(data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')
