from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg
import time
#from psycopg.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:
    try:
     conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='admin')
     cursor = conn.cursor()
     print("Database connection was successfull!")
     break
    except Exception as error:
     print("Connecting to database failed")
     print("Error", error)
     time.sleep(2)

# store in memory
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": 
"favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
 for p in my_posts:
   if p["id"] == id:
    return p
   
def find_index_post(id):
   for i, p in enumerate(my_posts):
      if p['id']==id:
         return i

@app.get("/")
def root(): #root where the API reside
    return {"message": "Welocome to my API!!"}


@app.get("/posts")
def get_posts():
   cursor.execute("""select * from posts""")
   post = cursor.fetchall()
   return {"data": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""insert into posts (title, content, published) values (%s, %s, %s) returning * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(""" select * from posts where id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
 
   cursor.execute(""" delete from posts where id = %s returning * """,(str(id),))
   deleted_post = cursor.fetchone()
   conn.commit()

   if deleted_post == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
   
   return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
   cursor.execute(""" update posts set title = %s, content = %s, published = %s where id = %s returning * """,(post.title, post.content, post.published,str(id)))
   
   updated_post = cursor.fetchone()
   conn.commit()

   if updated_post == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
   
 
   return {'data': updated_post}


