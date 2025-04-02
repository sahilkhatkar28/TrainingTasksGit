from src.config import db
from src.models.all_models import Users
from src.baground_tasks.celery_tasks import send_registration_email

class UserRegistration:
    @staticmethod
    def register(data):
        if not isinstance(data, dict):
            return {'status': 'error', 'statusCode': 400, 'message': 'Invalid JSON format'}, 400

        if 'username' not in data or 'email' not in data:
            return {'status': 'error', 'statusCode': 400, 'message': 'Username and email are required'}, 400

        username = data.get('username')
        email = data.get('email')
        print(f"Registering user: {username}, {email}")  # Debugging

        try:
            new_user = Users(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            send_registration_email.delay(email, username)
            return {'status': 'success', 'statusCode': 201, 'message': 'User Created Successfully'}, 201
        except Exception as e:
            db.session.rollback()
            return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
