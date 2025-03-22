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