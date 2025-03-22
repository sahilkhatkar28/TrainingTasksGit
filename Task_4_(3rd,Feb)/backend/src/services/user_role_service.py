from src.models.all_models import User,get_db
from flask_jwt_extended import create_access_token
from src.config.config import bcrypt
import uuid 

def signup(data):
    try:
        if 'username' in data and 'email' in data and 'password' in data:
            username = data['username']
            email = data['email']
            password = data['password']
           
            # Hash the password using bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            role = data.get('role','user')
            # Get a database connection
            db = get_db()
            User.create_table()

            # Insert new user into the 'users' table
            db.execute("INSERT INTO users (id, username, email, password, role) VALUES (?, ?, ?, ?, ?)",
                       (str(uuid.uuid4()), username, email, hashed_password,role))
            db.commit()
            db.close()

            return {'status': 'success', 'statusCode': 201, 'message': 'User Created Successfully'}, 201
        else:
            return {'status': 'error', 'statusCode': 400, 'message': 'Username, email, and password are required'}, 400

    except Exception as e:
        db.rollback()  # Rollback any changes in case of error
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500
    




def login(data):
    try:
        if 'email' in data and 'password' in data:
            email = data['email']
            password = data['password']

            # Get a database connection
            db = get_db()

            # Query the user by email
            user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

            if user and bcrypt.check_password_hash(user['password'], password):
                access_token = create_access_token(identity=user['id'])
                user_id = user['id']
                return {'status': 'success', 'statusCode': 200, 'message': 'Login Successful', 'token': access_token, "user":user_id}, 200
            else:
                return {'status': 'error', 'statusCode': 401, 'message': 'Invalid Credentials'}, 401

        else:
            return {'status': 'error', 'statusCode': 400, 'message': 'Email and password are required'}, 400

    except Exception as e:
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error occurred', 'error': str(e)}, 500







