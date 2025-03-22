from flask import Blueprint
from src.controllers.record_role_controller import get_users, get_user, update_user, delete_user

# Define the Blueprint for record-related routes
records_bp = Blueprint("records_bp", __name__)

# Define CRUD routes for user records
records_bp.route("/users", methods=["GET"])(get_users)
records_bp.route("/users/<id>", methods=["GET"])(get_user)
records_bp.route("/users/<id>", methods=["PUT"])(update_user)
records_bp.route("/users/<id>", methods=["DELETE"])(delete_user)
