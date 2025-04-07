from flask import request ,jsonify
from src.services.notification_service import NotificationService
from flask_jwt_extended import jwt_required

@jwt_required()
def notify():
    return jsonify(NotificationService.get_notifications())