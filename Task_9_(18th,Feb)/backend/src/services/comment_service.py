from src.models.comment_model import Comment, db
import uuid

def add_comment(data):
    try:
        if 'post_id' in data and 'user_id' in data and 'content' in data:
            new_comment = Comment(
                id=str(uuid.uuid4()),
                post_id=data['post_id'],
                user_id=data['user_id'],
                content=data['content']
            )
            db.session.add(new_comment)
            db.session.commit()

            return {'status': 'success', 'statusCode': 201, 'message': 'Comment added successfully'}, 201
        else:
            return {'status': 'error', 'statusCode': 400, 'message': 'Post ID, user ID, and content are required'}, 400
    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500

def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return [{'id': comment.id, 'content': comment.content, 'user_id': comment.user_id} for comment in comments], 200

def delete_comment(comment_id, user_id):
    try:
        comment = Comment.query.get(comment_id)
        if not comment:
            return {'status': 'error', 'statusCode': 404, 'message': 'Comment not found'}, 404
        if comment.user_id != user_id:
            return {'status': 'error', 'statusCode': 403, 'message': 'Unauthorized action'}, 403

        db.session.delete(comment)
        db.session.commit()
        return {'status': 'success', 'statusCode': 200, 'message': 'Comment deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
