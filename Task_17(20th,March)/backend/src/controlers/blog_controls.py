from flask import request  ,Response ,json , jsonify , g
from src.services import post_service
from flask_jwt_extended import jwt_required 

@jwt_required()
def createpost():
    data = request.json
    response,status = post_service.create_blog(data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')

@jwt_required()
def getposts():
    result = post_service.get_all_posts() 
    if isinstance(result, tuple):  # ✅ Check if it's a tuple
        response, status = result
    else:
        response, status = {"message": "Unexpected error"}, 500  # Fallback in case of issues

    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@jwt_required()
def updatepost(post_id):
    data = request.json
    response,status = post_service.update_post(post_id,data)
    return Response(response=json.dumps(response),status=status,mimetype='application/json')

@jwt_required()
def deletepost(post_id):
    
    response,status = post_service.delete_post(post_id)
    return Response(response=json.dumps(response),status=status,mimetype='application/json') 