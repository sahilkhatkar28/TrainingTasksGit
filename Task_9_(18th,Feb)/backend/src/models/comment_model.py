from src.config.config import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)  # Match UUID type

    post_id = db.Column(db.String(36), db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.date_posted}')"

class Like(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.String(36), db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Like(User: {self.user_id}, Post: {self.post_id})"
