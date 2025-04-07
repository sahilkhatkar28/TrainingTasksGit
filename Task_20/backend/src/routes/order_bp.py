from flask import Blueprint
from src.controller.order_controller import place_order

order_bp = Blueprint('order_bp',__name__)

order_bp.route('/place',methods=['POST'])(place_order)