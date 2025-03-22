from src.config.config import create_app
from src.routes.user_bp import user_bp


app = create_app()
app.register_blueprint(user_bp,url_prefix='/users')

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5001)  