from functools import wraps
from flask import request, jsonify
import sqlite3

def get_user_role(id):
    conn = sqlite3.connect('task4.db')
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    conn.close()
    
    return user[0] if user else None

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = request.headers.get('User-ID')  # Check if User-ID is provided
            if not user_id:
                return jsonify({"error": "User ID is missing in headers. Please include 'User-ID' in the request headers."}), 403
            
            user_role = get_user_role(user_id)
            if user_role is None:
                return jsonify({"error": "Invalid User ID. User does not exist."}), 403
            
            if user_role != required_role:
                return jsonify({"error": "Unauthorized access"}), 403

            return f(*args, **kwargs)
        return decorated_function
    return decorator
