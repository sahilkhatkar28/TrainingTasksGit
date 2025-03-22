from src.models.all_models import Comment, db
from datetime import datetime

class CommentService:

    @staticmethod
    def create_comment(data):
        try:
            if 'content' in data and 'post_id' in data:
                new_comment = Comment(
                    content=data['content'],
                    post_id=data['post_id'],
                    timestamp=datetime.utcnow()
                )
                db.session.add(new_comment)
                db.session.commit()

                return {'status': 'success', 'statusCode': 201, 'message': 'Comment Added Successfully'}, 201
            else:
                return {'status': 'error', 'statusCode': 400, 'message': 'Content and post ID are required'}, 400

        except Exception as e:
            db.session.rollback()
            return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500

    @staticmethod
    def get_comments(post_id):
        try:
            comments = Comment.query.filter_by(post_id=post_id).all()
            print(f"DEBUG: Found {len(comments)} comments for post_id {post_id}")  # Debugging

            return [{'id': comment.id, 'content': comment.content} for comment in comments]

        except Exception as e:
            return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
