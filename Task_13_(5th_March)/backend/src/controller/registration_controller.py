from flask import request , jsonify
from src.services.user_registration import UserRegistration
def register_user():
    data = request.get_json()  # Ensure JSON is properly parsed
    print("Received Data:", data)  # Debugging
    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data", "statusCode": 400}), 400
    return jsonify(UserRegistration.register(data))
