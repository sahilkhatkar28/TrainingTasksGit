import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///images.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB file size limit
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
