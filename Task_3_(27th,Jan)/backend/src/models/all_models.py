from src.config.database import get_db

class User:
    '''
    A class representing the user model for sqlite3 database operations.
    '''
    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def create_table():
        '''
        Creates the 'users' table if it does not exist.
        '''
        db = get_db()
        db.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id Text PRIMARY KEY,
                   username Text NOT NULL,
                   email Text NOT NULL UNIQUE,
                   password Text NOT NULL
                   )
                 ''')
        db.commit()

    @staticmethod
    def add_user(id,username,email,password):
        '''
        Adds a new user to the database
        '''
        db = get_db()
        try:
            db.execute("""
            INSERT INTO users (id,username,email,password)
            VALUES (?,?,?,?)
                       """, (id,username,email,password))
            db.commit()
        except Exception as e :
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