from src.model.post_db import Post , get_db
from flask_jwt_extended import get_jwt_identity
from src.config.config import bcrypt
import uuid
import sqlite3

def create_blog(data):
    try:
        if 'title' in data and 'content' in data:
            title = data['title']
            content = data['content']
            user_id = get_jwt_identity()
            id = str(uuid.uuid4())
            db = get_db()
            Post.create_post_table()

            db.execute('INSERT INTO posts (id,title,content,user_id) VALUES (?,?,?,?)', (id, title, content, user_id))
            db.commit()
            db.close()
            return {'message': 'Blog created successfully',"post_id":id}, 201
        else:
            return {'message': 'Invalid data'}, 400
    except Exception as e:
            print(e)
            return {'message': 'Error creating blog'}, 500
    


def get_all_posts():
    try:
        user_id = get_jwt_identity()  

        db = get_db()
        db.row_factory = sqlite3.Row  

        cursor = db.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,))
        posts = cursor.fetchall()

        if not posts:
            return {"message": "No posts found"}, 404 

        post_list = [
            {"id": row["id"], "title": row["title"], "content": row["content"], "user_id": row["user_id"]}
            for row in posts
        ]

        return {"posts": post_list}, 200 

    except Exception as e:
        print("Error:", e)
        return {"message": "Error fetching blogs"}, 500
     

def update_post(post_id,data ):     
     try:     
          if 'title' in data and 'content' in data :
               title = data['title']
               content = data['content']
               
               user_id = get_jwt_identity()
               db = get_db()
               db.execute('UPDATE posts SET title = ?, content = ? WHERE id = ? AND user_id = ?', (title, content, post_id, user_id))
               db.commit()
               db.close()
               return {'message': 'Blog updated successfully'}, 200
          else:
               return {'message': 'Invalid data'}, 400
     except Exception as e:
                
                return {'message': 'Error updating blog'}, 500


def delete_post(post_id):
     try:
         
              
               user_id = get_jwt_identity()
               db = get_db()
               db.execute('DELETE FROM posts WHERE id = ? AND user_id = ?', (post_id, user_id))
               db.commit()
             
               return {'message': 'Blog deleted successfully'}, 200
               
        
     except Exception as e:
           
            return {'message': 'Error deleting blog'}, 500
