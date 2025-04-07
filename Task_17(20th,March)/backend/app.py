from src.config.config import create_app
from src.routes.user_bp import user_bp
from src.routes.post_bp import post_bp


app = create_app()
app.register_blueprint(user_bp,url_prefix='/users')
app.register_blueprint(post_bp,url_prefix='/posts')

if __name__ == '__main__':
    app.run(debug=True) 