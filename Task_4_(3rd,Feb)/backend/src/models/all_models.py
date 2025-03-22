from src.config.database import get_db


class User:
    """
    A class representing the User model for SQLite3 database operations.
    """

    def __init__(self, id, username, email, password,role):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    @staticmethod
    def create_table():
        """
        Creates the 'users' table if it does not exist.
        """
        db = get_db()
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user'       
        )
        """)
        db.commit()

    @staticmethod
    def add_user(id, username, email, password,role):
        """
        Adds a new user to the database.
        """
        db = get_db()
        try:
            db.execute("""
            INSERT INTO users (id, username, email, password,role)
            VALUES (?, ?, ?, ?,?)
            """, (id, username, email, password,role))
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

    

    @staticmethod
    def get_user(id):
        """
        Fetches a user by their ID.
        """
        db = get_db()
        user = db.execute("""
        SELECT * FROM users WHERE id = ?
        """, (id,)).fetchone()
        return user

    @staticmethod
    def update_password(email, new_password):
        """
        Updates a user's password by their email.
        """
        db = get_db()
        try:
            db.execute("""
            UPDATE users SET password = ? WHERE email = ?
            """, (new_password, email))
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

 

    @staticmethod
    def delete_user(id):
        """
        Deletes a user by their email.
        """
        db = get_db()
        try:
            db.execute("""
            DELETE FROM users WHERE email = ?
            """, (id,))
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
