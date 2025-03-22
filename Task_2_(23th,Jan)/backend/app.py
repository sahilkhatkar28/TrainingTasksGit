from src.config.config import create_app
from src.routes.user_role_routes import user_bp
from src.routes.password_reset_routes import password_reset_bp


app = create_app()
app.register_blueprint(user_bp,url_prefix='/users')
app.register_blueprint(password_reset_bp,url_prefix='/password')

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5012)  