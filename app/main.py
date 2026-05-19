from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import User, Post
from .crawler import crawl_website
from .ai_pipeline import analyze_sentiment

# Perintah untuk membuat tabel otomatis di PostgreSQL saat API dinyalakan
Base.metadata.create_all(bind=engine)

# Inisialisasi FastAPI
app = FastAPI(title="AI Backend Pipeline")

# 1. Endpoint Cek Status
@app.get("/")
def check_status():
    return {"message": "Sistem API Aktif!"}

# 2. Endpoint Utama (Proses Ingestion + Crawling + AI)
@app.post("/ingest")
def proses_data_ingestion(username: str, url_target: str, db: Session = Depends(get_db)):
    # LANGKAH A: Daftarkan atau cari user di database
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
        
    # LANGKAH B: Jalankan mesin crawler untuk ambil teks dari internet
    teks_mentah = crawl_website(url_target)
    
    # LANGKAH C: Oper teks mentah ke mesin AI untuk dianalisis sentimennya
    hasil_ai = analyze_sentiment(teks_mentah)
    
    # LANGKAH D: Simpan gabungan data teks dan hasil AI ke database PostgreSQL
    data_baru = Post(content=teks_mentah, sentiment=hasil_ai, user_id=user.id)
    db.add(data_baru)
    db.commit()
    
    # LANGKAH E: Kirim laporan sukses kembali ke pengguna API
    return {
        "status": "Sukses diolah!",
        "oleh_user": user.username,
        "teks_terambil": teks_mentah,
        "analisis_ai_nlp": hasil_ai
    }
