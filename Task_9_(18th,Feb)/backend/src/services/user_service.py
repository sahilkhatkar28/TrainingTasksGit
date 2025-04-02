from src.models.user_model import User, db
from flask_jwt_extended import create_access_token
from src.config.config import bcrypt
import uuid

def signup(data):
    try:
        if 'username' in data and 'email' in data and 'password' in data:
            username = data['username']
            email = data['email']
            password = data['password']

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(
                id=str(uuid.uuid4()),
                username=username,
                email=email,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()

            return {'status': 'success', 'statusCode': 201, 'message': 'User Created Successfully'}, 201
        else:
            return {'status': 'error', 'statusCode': 400, 'message': 'Username, email, and password are required'}, 400

    except Exception as e:
        db.session.rollback()    
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
    
def login(data):
    try:
        if 'email' in data and 'password' in data:
            user = User.query.filter_by(email=data['email']).first()

            if user and bcrypt.check_password_hash(user.password, data['password']):
                access_token = create_access_token(identity=user.id)
                return {'status': 'success', 'statusCode': 200, 'message': 'Login Successful', 'token': access_token}, 200
            else:
                return {'status': 'error', 'statusCode': 401, 'message': 'Invalid Credentials'}, 401
    except Exception as e:
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
