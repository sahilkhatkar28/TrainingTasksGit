from flask import Blueprint
from src.controller.notification_controller import notify

notify_bp = Blueprint('notify_bp', __name__)
notify_bp.route('/notify', methods=['GET'])(notify) 