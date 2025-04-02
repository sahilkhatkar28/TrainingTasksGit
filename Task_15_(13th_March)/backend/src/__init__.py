from flask import Flask
from src.config import Config
from src.database import db
from src.routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Ensure tables are created

    init_routes(app)

    return app
