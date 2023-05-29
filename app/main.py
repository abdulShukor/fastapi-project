from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
from sqlalchemy.orm import Session
import psycopg
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth
#from psycopg.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root(): #root where the API reside
    return {"message": "Welocome to my API!!"}

