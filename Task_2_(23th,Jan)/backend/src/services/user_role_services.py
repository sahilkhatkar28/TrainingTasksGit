from src.models.all_model import User,get_db
from flask_jwt_extended import create_access_token
from src.config.config import bcrypt
import uuid

def signup(data):
    try:
        if 'username' in data and 'email' in data and 'password' in data:
            username= data['username']
            email = data['email']
            password = data['password']

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            db = get_db()
            User.create_table()

            db.execute('INSERT INTO users(id,username,email,password) VALUES (?,?,?,?)',
                       (str(uuid.uuid4()),username,email,hashed_password))
            db.commit()
            db.close()
            return {'status':'sucess','statuscode':201,'message':'user created successfully'},201
        else:
            return {'status':'failed','statuscode':400,'message':'username,email,password are required'},400
        
    except Exception as e :
        db.rollback()
        return {'status':'failed','statuscode':500,'message':'Error accoured','error':str(e)},500
    


def login(data):
    try:
        if 'email' in data and 'password' in data:
            email = data['email']
            password = data['password']

            db = get_db()
            user = db.execute("SELECT * FROM users WHERE email = ?",(email,)).fetchone()

            if user and bcrypt.check_password_hash(user['password'],password):
                access_token = create_access_token(identity=user['id'])
                return {'status':'success','statuscode':200,'message':'login successful','token':access_token},200
            else:
                return {'status':'failed','statuscode':401,'message':'invalid credentials'},401
        else:
            return {'status':'failed','statuscode':400,'message':'email and password are required'},400
        
    except Exception as e:
        return {'status':'failed','statuscode':500,'message':'Error accoured','error':str(e)},500
    



            