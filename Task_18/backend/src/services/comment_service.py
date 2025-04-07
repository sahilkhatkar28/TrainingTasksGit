from src.models.all_models import Comment,db
from datetime import datetime
from flask_jwt_extended import  get_jwt_identity
import uuid

class CommentService:

    @staticmethod
    def create_comment(data):
        try:
            if 'post_name' in data and 'content' in data:
                current_user = get_jwt_identity()
                new_comment = Comment(
                    post_name=data['post_name'],
                    content=data['content'],
                    user_id=current_user,
                     id = str(uuid.uuid4()),
                     created_at=datetime.utcnow()
                )
                db.session.add(new_comment)
                db.session.commit()
            

                return {
                    'message': 'Comment created successfully'
                        },201
            else:
                return {'message':'invalid data'},400

        except Exception as e:
            db.session.rollback()
            print(e)
            return {'message':'failed to create comment'},500

    @staticmethod
    def get_comments(post_name):
        try:
            comments = Comment.query.filter_by(post_name=post_name).all()
            return [{"user":comment.user_id, "content":comment.content} for comment in comments]

        except Exception as e:
            print(e)
            return {'message':'failed to get comments'},500

