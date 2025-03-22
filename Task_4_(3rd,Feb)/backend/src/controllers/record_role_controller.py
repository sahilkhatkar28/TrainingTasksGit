from flask import request, Response, json
from src.services import records_role_service
from flask_jwt_extended import jwt_required

@jwt_required()
def get_users():
    response, status = records_role_service.get_users()
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def get_user(id):
    response, status = records_role_service.get_user(id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def update_user(id):
    data = request.json
    response, status = records_role_service.update_user(id, data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def delete_user(id):
    response, status = records_role_service.delete_user(id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')


