from src.model.user_db import User , get_db
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

            db = get_db()
            User.create_table()

            db.execute('INSERT INTO users(id,username,email,password) VALUES(?,?,?,?)',
                       (str(uuid.uuid4()), username, email, hashed_password))
            
            db.commit()
            return {'message': 'User created successfully'}, 201
        else:
            return {'message': 'Invalid data'}, 400
        
    except Exception as e :
        db.rollback()
        print(e)
        return {'message': str(e)}, 500
        
    



def login(data):
    try:
        if 'email' in data and 'password' in data:
            email = data['email']
            password = data['password']
            db = get_db()
            user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

            if user and bcrypt.check_password_hash(user['password'],password):
                access_token = create_access_token(identity=user['id'])
                return {'token': access_token}, 200
            else:
                return {'message': 'Invalid credentials'}, 401
        else:
            return {'message': 'Invalid data'}, 400
        
    except Exception as e:
        return {'message': str(e)}, 500
    