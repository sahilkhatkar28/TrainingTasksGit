from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import User
from app.models import db

class AuthService:
    @staticmethod
    def register_user(username, password):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None
