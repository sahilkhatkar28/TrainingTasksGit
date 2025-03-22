# password_reset_controller.py
from flask import request, json,jsonify, url_for, Response
from src.services.password_reset_service import request_password_reset, send_reset_email, reset_password

def request_password_reset_controller():
    try:
        data = request.get_json()
        email = data.get("email")
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        token = request_password_reset(email)
        if isinstance(token, tuple):
            return jsonify(token[0]), token[1]
        
        reset_url = url_for('password_reset_bp.reset_password_controller', token=token, _external=True)
        send_reset_email(email, reset_url)
        
        return jsonify({"message": "Password reset email sent"}), 200
    except Exception as e:
        print(f"Error in request_password_reset_controller: {e}")
        return jsonify({"error": "Internal server error"}), 500

def reset_password_controller(token):
    try:
        data = request.get_json()
        new_password = data.get("password")
        
        response, status = reset_password(token, new_password)
        return Response(response=json.dumps(response), status=status, mimetype='application/json')
    except Exception as e:
        print(f"Error in reset_password_controller: {e}")
        return jsonify({"error": "Internal server error"}), 500
