from transformers import pipeline

# Memuat model AI siap pakai untuk Analisis Sentimen
nlp_ai = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str) -> str:
    try:
        # AI membaca teks dan memberikan hasil
        result = nlp_ai(text)
        return result[0]['label'] # Menghasilkan teks: 'POSITIVE' atau 'NEGATIVE'
    except Exception:
        return "NEUTRAL"
