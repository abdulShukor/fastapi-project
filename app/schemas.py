from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
   #  rating: Optional[int] = None

class PostCreate(PostBase):
    pass

# pythan execute code line by line, UerOut should be before the Post model to avoid error

class UserOut(BaseModel):
   id: int
   email: EmailStr
   created_at: datetime

   class Config:
     orm_mode = True

class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: UserOut

  class Config:
     orm_mode = True
class PostOut(BaseModel):
  Post: Post
  votes: int

  class Config:
   orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
   email: EmailStr
   password: str

class Token(BaseModel):
   access_token: str
   token_type: str

class TokenData(BaseModel):
    id: Optional[str]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    # allow 1,0
    #it also allow negative value
    