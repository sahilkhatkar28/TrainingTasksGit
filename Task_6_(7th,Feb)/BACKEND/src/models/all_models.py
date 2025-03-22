from src.config.config import db
from datetime import datetime



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)  # UUID as primary key
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Hashed password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with Post
    posts = db.relationship("Post", backref="author", lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign Key: User ID
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    # Relationship with Comment
    comments = db.relationship("Comment", backref="post", lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<Post {self.title}>"


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key: Post ID
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"<Comment {self.id}>"
