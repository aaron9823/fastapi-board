from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.post import Post
from app.services import post_service
from app.db.database import get_db

router = APIRouter()

# Retrieve all posts
@router.get("/posts", response_model=List[Post])
def get_posts(db: Session = Depends(get_db)):
    return post_service.get_all_posts(db)

# Create a new post
@router.post("/posts", response_model=Post)
def create_post(post: Post, db: Session = Depends(get_db)):
    return post_service.create_post(post, db)

# Update an existing post by ID
@router.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, updated_post: Post, db: Session = Depends(get_db)):
    return post_service.update_post(post_id, updated_post, db)

# Delete a post by ID
@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.delete_post(post_id, db)
