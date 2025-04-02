from src.config.config import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.String(36), primary_key=True)  # Changed to match UUID format
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)  # Match UUID type

    # Relationships
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete")
    likes = db.relationship('Like', backref='post', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"Post(id='{self.id}', title='{self.title}', user_id='{self.user_id}', date='{self.date_posted}')"
