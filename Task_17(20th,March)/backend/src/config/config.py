from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

bcrypt = Bcrypt()
jwt = JWTManager()


class Config:
    SECRET_KEY = "your_secret_key"
    DATABASE = 'task17.db'
    JWT_SECRET_KEY = "your_jwt_secret_key"
    
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from src.config.database import close_db
    app.teardown_appcontext(close_db)



    CORS(app)

   
    bcrypt.init_app(app)
    jwt.init_app(app)


    return app
