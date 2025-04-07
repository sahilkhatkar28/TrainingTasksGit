from flask import Blueprint
from src.controller.follow_controller import follow_user,unfollow_user,get_followers,get_following

follow_bp = Blueprint('follow_bp',__name__)

follow_bp.route('/follow/<string:user_username>',methods =['POST'])(follow_user)
follow_bp.route('/unfollow/<string:user_username>',methods =['DELETE'])(unfollow_user) 
follow_bp.route('/followers',methods =['GET'])(get_followers)
follow_bp.route('/following',methods =['GET'])(get_following)  