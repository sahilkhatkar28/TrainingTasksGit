from src.config.database import get_db

class User :
    '''
    Creates the 'User' table if does not exists.
    '''
    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def create_table():

         db = get_db()
         db.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id Text PRIMARY KEY,
            username Text NOT NULL,
            email Text NOT NULL UNIQUE,
            password Test NOT NULL
               )

              ''')
         db.commit() 


    @staticmethod
    def add_user(id,username,email,password):
        db = get_db()
        try:
            db.execute(''' 
              INSERT INTO users(id,username,email,password)
              VALUES (?,?,?,?)  ''',
               (id,username,email,password))
            db.commit()

        except Exception as e:
            db.rollback()
            raise e 
