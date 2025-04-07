from flask import request , jsonify
from src.services.order_service import OrderService
from flask_jwt_extended import jwt_required

@jwt_required()
def place_order():
    data = request.json
    return jsonify(OrderService.place_order(data))
