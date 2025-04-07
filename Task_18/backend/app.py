from src.config.config import create_app,db

from src.routes.user_routes import user_bp
from src.routes.follow_routes import follow_bp
from src.routes.post_routes import post_bp
from src.routes.comment_routes import comment_bp
from src.routes.notification_routes import notify_bp

app = create_app()

app.register_blueprint(user_bp,url_prefix='/users')
app.register_blueprint(follow_bp,url_prefix='/follows')
app.register_blueprint(post_bp,url_prefix='/post')
app.register_blueprint(comment_bp,url_prefix='/comment')
app.register_blueprint(notify_bp,url_prefix='/notification')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)    