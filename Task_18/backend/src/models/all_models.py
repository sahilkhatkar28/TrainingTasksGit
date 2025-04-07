from src.config.config import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.String(36) , primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    followers = db.relationship('Follow',backref='followed',lazy=True,foreign_keys = 'Follow.following_id')
    following = db.relationship('Follow', backref='follower',lazy=True,foreign_keys = 'Follow.follower_id')

class Follow(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    follower_id = db.Column(db.String(36), db.ForeignKey('user.username'),nullable =False)
    following_id = db.Column(db.String(36), db.ForeignKey('user.username'),nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Post(db.Model):
    name = db.Column(db.String(36), primary_key=True,unique=True,nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.username'),nullable = False)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    post_name = db.Column(db.String(36), db.ForeignKey('post.name'),nullable = False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.username'),nullable = False)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  


class Notification(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.username'),nullable = False)
    message = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

