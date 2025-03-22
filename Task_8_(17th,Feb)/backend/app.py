from flask import Flask
from src.config.config import Config
from src.models.models import db
from src.routes.routes import routes
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)

# Ensure upload folder exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
