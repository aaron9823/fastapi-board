from sqlalchemy import Column, Integer, String
from app.db.database import Base

# Define the Post table
class Post(Base):
    __tablename__ = "posts"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each post
    title = Column(String(255), nullable=False)  # Post title (maximum 255 characters, cannot be null)
    content = Column(String(500), nullable=False)  # Post content (maximum 500 characters, cannot be null)
