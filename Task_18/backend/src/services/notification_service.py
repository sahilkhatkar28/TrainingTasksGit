from src.models.all_models import Post ,Follow ,db
from flask_jwt_extended import get_jwt_identity

class NotificationService:

    @staticmethod
    def get_notifications():
        try:
            user_id = get_jwt_identity()
            following = Follow.query.filter_by(follower_id = user_id).all()
            following_ids = [follow.following_id for follow in following]


            posts = (
                Post.query.filter(Post.user_id.in_(following_ids)).order_by(Post.created_at.desc()).limit(10).all()
                )

            return { 'post':[{'name':post.user_id,'post_name':post.name ,"content":post.content ,"created_at":post.created_at} for post in posts]}

        except Exception as e:
            print(e)
            return {'message':'error in get notifications'},500
        
