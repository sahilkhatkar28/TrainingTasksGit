
from src.config.config import create_app,db
from src.routes.user_routes import user_bp
from src.routes.post_routes import post_bp
from src.routes.comment_routes import comment_bp


app = create_app()



# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')
app.register_blueprint(comment_bp, url_prefix='/comment')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5016)  
        
