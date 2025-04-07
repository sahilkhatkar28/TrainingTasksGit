from flask import Blueprint
from src.controller.product_controller import add, update , get


product_bp = Blueprint('product_bp',__name__)

product_bp.route("/add",methods=['POST'])(add)
product_bp.route("/update",methods=['PUT'])(update)
product_bp.route("/get",methods=['GET'])(get)  