from sqlalchemy.orm import Session
from app.models.post import Post
from app.db.database import get_db
from fastapi import Depends, HTTPException
from typing import List

def get_all_posts(db: Session) -> List[Post]:
    """Retrieve all posts"""
    return db.query(Post).all()

def create_post(post: Post, db: Session):
    """Add a new post"""
    db.add(post)
    db.commit()
    db.refresh(post)  # Refresh the post instance to reflect database changes
    return post

def update_post(post_id: int, updated_post: Post, db: Session):
    """Update an existing post"""
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Update post fields
    db_post.title = updated_post.title
    db_post.content = updated_post.content
    db.commit()
    db.refresh(db_post)  # Refresh the updated post instance
    return db_post

def delete_post(post_id: int, db: Session):
    """Delete a post"""
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}
