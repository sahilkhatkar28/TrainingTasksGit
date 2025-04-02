from src.models.comment_model import Like, db
import uuid

def like_post(post_id, user_id):
    try:
        existing_like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()
        if existing_like:
            return {'status': 'error', 'statusCode': 400, 'message': 'Post already liked'}, 400
        
        
        new_like = Like(id=str(uuid.uuid4()), post_id=post_id, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()

        return {'status': 'success', 'statusCode': 201, 'message': 'Post liked successfully'}, 201
    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500

def unlike_post(post_id, user_id):
    try:
        like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()
        if not like:
            return {'status': 'error', 'statusCode': 404, 'message': 'Like not found'}, 404

        db.session.delete(like)
        db.session.commit()
        return {'status': 'success', 'statusCode': 200, 'message': 'Post unliked successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
