from flask import request, jsonify
from src.services import get_paginated_products, add_product

def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category', None)
    search = request.args.get('search', None)

    data = get_paginated_products(page, per_page, category, search)
    return jsonify(data)

def create_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    products = add_product(data)

    if isinstance(products, list):
        return jsonify({"message": f"{len(products)} products added successfully"}), 201

    return jsonify({"message": "Product added successfully", "product": products.to_dict()}), 201
