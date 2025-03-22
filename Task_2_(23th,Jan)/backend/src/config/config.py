from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail



bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()



class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret-key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sakh2810@gmail.com'
    MAIL_PASSWORD = 'sdxvbzcajqexkucp'
    MAIL_DEFAULT_SENDER = 'sakh2810@gmail.com'
    DATABASE = 'task2.db'









def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from src.config.database import close_db
    app.teardown_appcontext(close_db)

    CORS(app)

    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)


    return app



