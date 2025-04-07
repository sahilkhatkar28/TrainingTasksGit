from src.config.database import get_db

class Post():

    def __init__(self, title, content, user_id,id):

        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id  


    @staticmethod
    def create_post_table():
        db = get_db()
        db.execute( ''' 
        CREATE TABLE IF NOT EXISTS posts (
        id Text PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        user_id TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                   )
        ''' )


    @staticmethod
    def create_post(id,title, content,user_id):
        db = get_db()
        try:
            db.execute('''
            INSERT INTO posts (id,title,content,user_id) VALUES (?,?,?,?)''', (id,title,content,user_id))
            db.commit()

        except Exception as e :
            db.rollback()
            raise e

    


