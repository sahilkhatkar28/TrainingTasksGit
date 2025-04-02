from flask import Flask
from app.config.config import Config
from app.models import db
from app.sockets.socket_events import socketio
from app.routes.auth_routes import auth_bp
from app.routes.chat_routes import chat_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    socketio.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)

    return app
