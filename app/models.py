from sqlalchemy import Column, Integer, String, ForeignKey, Text
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)         # Tempat menyimpan teks hasil crawl
    sentiment = Column(String)     # Tempat menyimpan hasil analisis AI (Positive/Negative)
    user_id = Column(Integer, ForeignKey("users.id")) # Menghubungkan post ke user-nya
