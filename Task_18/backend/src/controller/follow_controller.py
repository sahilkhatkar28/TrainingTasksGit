from flask import request , jsonify
from src.services.follow_service import FollowService
from flask_jwt_extended import jwt_required 

@jwt_required()
def follow_user(user_username):
    return jsonify(FollowService.follow(user_username))

@jwt_required()
def unfollow_user(user_username):
    return jsonify(FollowService.unfollow(user_username))

@jwt_required()
def get_followers():
    return jsonify(FollowService.followers())

@jwt_required()
def get_following():
    return jsonify(FollowService.following())  
    