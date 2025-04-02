from flask import Blueprint
from src.controllers import get_products, create_product

def init_routes(app):
    api = Blueprint('api', __name__)

    api.route('/products', methods=['GET'])(get_products)
    api.route('/products', methods=['POST'])(create_product)

    app.register_blueprint(api, url_prefix='/api')
