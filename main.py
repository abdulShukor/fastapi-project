from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": 
"favorite foods", "content": "I like pizza", "id": 2}]

@app.get("/")
def root():
    return {"message": "Welocome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.post("/posts")
def create_posts(post: Post):
    print(post.dict())
    return {"data": post}
#title str, content str,