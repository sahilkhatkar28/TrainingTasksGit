from src.config import create_app  # ✅ Import Flask app
from src.routes.registration_routes import user_bp

app = create_app()
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)  # ✅ Run the Flask app in debug mode
