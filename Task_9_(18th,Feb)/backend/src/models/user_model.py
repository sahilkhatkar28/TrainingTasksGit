from src.config.config import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True) 
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Store hashed password

    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete")
    comments = db.relationship('Comment', backref='user', lazy=True, cascade="all, delete")
    likes = db.relationship('Like', backref='user', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"