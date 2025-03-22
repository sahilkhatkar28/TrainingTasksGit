from flask import Blueprint
from src.controllers.password_reset_controller import request_password_reset_controller, reset_password_controller

# Define the Blueprint for password reset-related routes
password_reset_bp = Blueprint("password_reset_bp", __name__)

# Define password reset routes
password_reset_bp.route("/request", methods=["POST"])(request_password_reset_controller)
password_reset_bp.route("/reset/<token>", methods=["GET","POST"])(reset_password_controller)
