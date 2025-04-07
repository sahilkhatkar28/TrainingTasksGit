from flask import request , jsonify
from src.services.product_service import ProductService
from flask_jwt_extended import jwt_required

@jwt_required()
def add():
    data = request.json
    return jsonify(ProductService.add_product(data))

@jwt_required()
def update():
    data = request.json
    return jsonify(ProductService.update_product(data))

@jwt_required()
def get():
    return jsonify(ProductService.get_all_product())