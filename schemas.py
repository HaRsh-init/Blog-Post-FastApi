from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: EmailStr = Field(max_length=100)

class UserCreate(UserBase):
    #password: str = Field(min_length=6, max_length=100)
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    image_file: str | None
    image_path: str

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=100)
    image_file: str | None = Field(default=None)


class PostBase(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)

class PostUpdate(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    title: str | None = Field(default= None, min_length=1, max_length=100)
    content: str | None = Field(default= None, min_length=1)

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int = Field()
    user_id: int = Field()
    date_posted: datetime = Field()
    author: UserResponse