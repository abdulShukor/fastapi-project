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
    cursor.execute("""insert into posts""")
    
    return {"data": "created post"}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
   # delete post
   index = find_index_post(id)
   if index == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id does not exist')
   my_posts.pop(index)
   return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
   index = find_index_post(id)
   if index == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id does not exist')
   
   post_dict = post.dict()
   post_dict['id'] = id
   my_posts[index] = post_dict
   return {'data': post_dict}


