from src.models.all_models import Post, db
from datetime import datetime

class PostService:

    @staticmethod
    def create_post(data):
        try:
            if 'title' in data and 'content' in data and 'user_id' in data:
                new_post = Post(
                    title=data['title'],
                    content=data['content'],
                    user_id=data['user_id'],
                    timestamp=datetime.utcnow()
                )
                db.session.add(new_post)
                db.session.commit()

                return {'status': 'success', 'statusCode': 201, 'message': 'Post Created Successfully'}, 201
            else:
                return {'status': 'error', 'statusCode': 400, 'message': 'Title, content, and user ID are required'}, 400

        except Exception as e:
            db.session.rollback()
            return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500

    @staticmethod
    def get_all_posts():
        posts = Post.query.all()
        return [{'id': post.id, 'title': post.title, 'content': post.content, 'author_id': post.user_id} for post in posts]
