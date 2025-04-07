from flask_bcrypt import generate_password_hash , check_password_hash
from src.models.all_models import User, db
from flask_jwt_extended import create_access_token
import uuid


class UserService:

    @staticmethod
    def signup(data):
        try:
            if 'username' in data and 'email' in data and 'password' in data :
                username = data['username']
                email = data['email']
                password = data['password']
                

                
                
                hashed_password = generate_password_hash(password).decode('utf-8')
                role = data.get('role', 'user')

                new_user = User(
                    id = str(uuid.uuid4()),
                    username = username,
                    email = email,
                    password = hashed_password,
                    role = role,
                )

                db.session.add(new_user)
                db.session.commit()
                return {'message': 'User created successfully'}, 201
            else:
                return {'message': 'Missing required fields'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @staticmethod
    def login(data):
        try:
            if 'email' in data and 'password' in data:
                email = data['email']
                password = data['password']
                user = User.query.filter_by(email = email).first()
                if user and check_password_hash(user.password, password):
                    access_token = create_access_token(identity = user.role)
                    return {'access_token': access_token}, 200
                else:
                    return {'message': 'Invalid credentials'}, 401
                
        except Exception as e :
            return {'message': str(e)}, 500