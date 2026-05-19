import requests
from bs4 import BeautifulSoup

def crawl_website(url: str) -> str:
    try:
        # Melakukan request ke website target
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Mengambil semua teks yang ada di dalam tag <p> (paragraf)
            paragraphs = [p.text for p in soup.find_all('p')]
            return " ".join(paragraphs)[:300] # Ambil 300 karakter pertama saja
    except Exception:
        pass
    # Jika web error/terblokir, ini adalah teks cadangan untuk simulasi
    return "Aplikasi back-end baru ini bekerja dengan sangat cepat, saya sangat menyukainya!"
