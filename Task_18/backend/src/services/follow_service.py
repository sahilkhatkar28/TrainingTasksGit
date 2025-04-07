from src.models.all_models import Follow ,db
from flask_jwt_extended import get_jwt_identity
import uuid

class FollowService:

    @staticmethod
    def follow(user_username):
        try:
            current_user_username = get_jwt_identity()
            if Follow.query.filter_by(follower_id = current_user_username, following_id = user_username).first():
                return {'message':'Already following'},400
            
            follow = Follow(follower_id = current_user_username, following_id = user_username,id=str(uuid.uuid4()))
            db.session.add(follow)
            db.session.commit()
            return {'message':'User followed'},200
        
        except Exception as e:
            print(e)
            return {'message':'Error'},500
        

    @staticmethod
    def unfollow(user_username):
        try:
            current_user_username = get_jwt_identity()
            follow = Follow.query.filter_by(follower_id = current_user_username, following_id = user_username).first()
            if not follow:
                return {'message':'Not following'},400
            
            db.session.delete(follow)
            db.session.commit()
            return {'message':'User unfollowed'},200
        
        except Exception as e:
            print(e)
            return {'message':'Error'},500
        

    @staticmethod
    def followers():
        try:
            current_user_username = get_jwt_identity()
            followers = Follow.query.filter_by(following_id = current_user_username).all()
            return {'followers':[follower.follower_id for follower in followers]},200
        except Exception as e:
            print(e)
            return {'message':'Error'},500
        


    @staticmethod
    def following():
        try:
            current_user_username = get_jwt_identity()
            following = Follow.query.filter_by(follower_id = current_user_username).all()
            return {'following':[follower.following_id for follower in following]},200
        except Exception as e:
            print(e)
            return {'message':'Error'},500
        
        
