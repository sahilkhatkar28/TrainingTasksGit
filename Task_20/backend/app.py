from src.config.config import create_app, db

from src.routes.user_bp import user_bp
from src.routes.product_bp import product_bp
from src.routes.order_bp import order_bp

app = create_app()

app.register_blueprint(user_bp,url_prefix = '/user')
app.register_blueprint(product_bp,url_prefix = '/product')
app.register_blueprint(order_bp,url_prefix = '/order')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)  