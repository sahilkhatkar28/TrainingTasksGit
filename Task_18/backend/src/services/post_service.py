from src.models.all_models import Post, db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity


class PostService:

    @staticmethod
    def create_post(data):
        try:
            if "name" in data and "content" in data :
                user_id = get_jwt_identity()
                new_post = Post (
                    name=data["name"],
                    content=data["content"],
                    user_id=user_id,
                    created_at=datetime.utcnow()

                )
                db.session.add(new_post)
                db.session.commit()

                return { "message": "Post created successfully", "post_id": new_post.name } , 201
            
            else:
                return {"message": "Invalid data"}, 400
            

        except Exception as e :
            db.session.rollback()
            return {"message": "Error creating post"}, 500
        

    @staticmethod
    def get_all_posts():
        try:
            current_user = get_jwt_identity()
            posts = Post.query.filter_by(user_id = current_user).all()
            return [{'post':post.name,'content':post.content,"time":post.created_at} for post in posts]
        
        except Exception as e:
            print(e)
            return {"message": "Error fetching posts"}, 500
