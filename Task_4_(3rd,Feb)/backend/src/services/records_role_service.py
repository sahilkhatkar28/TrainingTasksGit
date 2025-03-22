from src.models.all_models import get_db





def get_users():
    try:
        db = get_db()
        users = db.execute("SELECT id, username, email ,role FROM users").fetchall()
        db.close()

        user_list = [dict(user) for user in users]
        return {'status': 'success', 'statusCode': 200, 'data': user_list}, 200

    except Exception as e:
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error fetching users', 'error': str(e)}, 500


def get_user(id):
    try:
        db = get_db()
        user = db.execute("SELECT id, username, email ,role FROM users WHERE id = ?", (id,)).fetchone()
        db.close()

        if user:
            return {'status': 'success', 'statusCode': 200, 'data': dict(user)}, 200
        else:
            return {'status': 'error', 'statusCode': 404, 'message': 'User not found'}, 404

    except Exception as e:
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error fetching user', 'error': str(e)}, 500


def update_user(id, data):
    try:
        db = get_db()
        
        update_fields = []
        params = []
        
        if 'username' in data:
            update_fields.append("username = ?")
            params.append(data['username'])
        if 'email' in data:
            update_fields.append("email = ?")
            params.append(data['email'])

        if not update_fields:
            return {'status': 'error', 'statusCode': 400, 'message': 'No data provided to update'}, 400

        params.append(id)
        db.execute(f"UPDATE users SET {', '.join(update_fields)} WHERE id = ?", params)
        db.commit()
        db.close()

        return {'status': 'success', 'statusCode': 200, 'message': 'User updated successfully'}, 200

    except Exception as e:
        db.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error updating user', 'error': str(e)}, 500


def delete_user(id):
    try:
        db = get_db()
        db.execute("DELETE FROM users WHERE id = ?", (id,))
        db.commit()
        db.close()

        return {'status': 'success', 'statusCode': 200, 'message': 'User deleted successfully'}, 200

    except Exception as e:
        db.rollback()
        return {'status': 'failed', 'statusCode': 500, 'message': 'Error deleting user', 'error': str(e)}, 500
    

