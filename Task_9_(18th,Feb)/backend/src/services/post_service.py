from src.models.post_model import Post, db
import uuid

def create_post(data, user_id):
    try:
        if 'title' in data and 'content' in data:
            new_post = Post(
                id=str(uuid.uuid4()),
                title=data['title'],
                content=data['content'],
                user_id=user_id  # Now extracted from JWT
            )
            db.session.add(new_post)
            db.session.commit()

            return {'status': 'success', 'statusCode': 201, 'message': 'Post Created Successfully'}, 201
        else:
            return {'status': 'error', 'statusCode': 400, 'message': 'Title and content are required'}, 400

    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500

def get_all_posts():
    posts = Post.query.all()
    return [{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id,'comments': len(post.comments),'likes': len(post.likes)} for post in posts], 200

def delete_post(post_id, user_id):
    try:
        post = Post.query.get(post_id)
        if not post:
            return {'status': 'error', 'statusCode': 404, 'message': 'Post not found'}, 404
        if post.user_id != user_id:
            return {'status': 'error', 'statusCode': 403, 'message': 'Unauthorized action'}, 403

        db.session.delete(post)
        db.session.commit()
        return {'status': 'success', 'statusCode': 200, 'message': 'Post deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
