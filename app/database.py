from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Mengatur alamat database PostgreSQL
DATABASE_URL = "postgresql://postgres:password@localhost:5432/social_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # Ini adalah dasar untuk membuat tabel

# Fungsi untuk menyediakan sesi database ke API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
