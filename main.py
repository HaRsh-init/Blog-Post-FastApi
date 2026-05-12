from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlalchemy
from starlette.exceptions import HTTPException as StarletteHTTPException

from schemas import postCreate, postResponse, UserResponse, UserCreate, postUpdate

from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import get_db, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/", include_in_schema= False, name= "home")
@app.get("/posts", include_in_schema= False, name= "posts")
def home(request: Request, db: Annotated[Session, Depends(get_db)]):
    # Fetch posts from the database
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/posts/{post_id}", include_in_schema= False)
def post_page(request: Request,post_id: int, db: Annotated[Session, Depends(get_db)]):
    # Fetch the specific post from the database
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    title = post.title[:50]
    return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})

@app.get("/users/{user_id}", include_in_schema= False, name= "user_posts")
def user_posts_page(request: Request, user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Fetch the specific user from the database
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Fetch posts by the user
    result = db.execute(select(models.Post).where(models.Post.author_id == user_id))
    posts = result.scalars().all()

    title = f"{user.username}'s Posts"
    return templates.TemplateResponse(request, "user_posts.html", {"posts": posts, "title": title, "user": user})


@app.post("/api/users", response_model= UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    # Implementation for creating a user
    result = db.execute(select(models.User).where(models.User.username == user.username))#.scalar_one_or_none()
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User already exists")
    
    result = db.execute(select(models.User).where(models.User.email == user.email))#.scalar_one_or_none()
    existing_email = result.scalars().first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User already exists")
    
    new_user = models.User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/api/users/{user_id}", response_model= UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.User).where(models.User.id == user_id))#.scalar_one_or_none()
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.get("/api/users/{user_id}/posts", response_model= list[postResponse])
def get_user_posts(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.author_id == user_id))
    user = result.scalars().all()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found for this user")
    
    result= db.execute(select(models.Post).where(models.Post.author_id == user_id))#.scalar_one_or_none()
    posts = result.scalars().first()
    return posts


@app.get("/api/posts", response_model= list[postResponse])
def get_posts(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post))
    return result.scalars().all()


@app.post("/api/posts", response_model= postResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: postCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.User).where(models.User.id == post.user_id))#.scalar_one_or_none()
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/api/posts/{post_id}", response_model= postResponse)
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.put("/api/posts/{post_id}", response_model= postResponse)
def update_post(post_id: int, post_data: postUpdate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.id == post_id))#.scalar_one_or_none()
    post = result.scalars().first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    if post_data.user_id != post.user_id:
        result = db.execute(select(models.User).where(models.User.id == post_data.user_id))#.scalar_one_or_none()
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    post.title = post_data.title
    post.content = post_data.content
    post.user_id = post_data.user_id

    db.commit()
    db.refresh(post)
    return post

# StarletteHTTPException Handler
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )

### RequestValidationError Handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )

