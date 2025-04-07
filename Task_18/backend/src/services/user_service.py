from flask_bcrypt import generate_password_hash , check_password_hash
from src.models.all_models import User , db
from flask_jwt_extended import create_access_token
import uuid


class UserService:
    @staticmethod
    def signup(data):
        try:
            if 'username' in data and 'email' in data and 'password' in data:
                username = data['username']
                email = data['email']
                password = data['password']

                hashed_password = generate_password_hash(password).decode('utf-8')

                new_user = User(
                    id = str(uuid.uuid4()),
                    username = username,
                    email = email,
                    password = hashed_password
                )

                db.session.add(new_user)
                db.session.commit()

                return {'message':'user added successfully'},201
            else:
                return {'message':'invalid data'},400
            

        except Exception as e:
            db.session.rollback()
            print("error = ", e)
            return {'message':'error occurred'},500
        

    @staticmethod
    def login(data):
        try:
            if 'email' in data and 'password' in data:
                user = User.query.filter_by(email=data['email']).first()
                if user and check_password_hash(user.password , data['password']):
                    access_token = create_access_token(identity=user.username)
                    return {'message':'login successful','token':access_token},200
                else:
                    return {'message':'invalid credentials'},401
                
            else:
                return {'message':'invalid data'},400
        except Exception as e :
            print("error = ", e)
            return {'message':'error occurred'},500
        