import os
from google import genai
from dotenv import load_dotenv

# 1. .env dosyasındaki gizli şifreleri yükle
load_dotenv()

# 2. Gemini istemcisini başlat (Şifreyi otomatik çeker)
client = genai.Client()

print("Gemini'ye mesaj gönderiliyor (Ücretsiz Tier)...")

try:
    # 3. Gemini-2.5-Flash modeline mesaj gönderiyoruz
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Merhaba Gemini! Ben 60 günlük yapay zeka yolculuğuma başladım. Bana bu yolculuk için tek cümlelik harika bir tavsiye verir misin?',
    )

    # 4. Gelen canlı yanıtı ekrana yazdırıyoruz
    print("\n--- Gemini'nin Cevabı ---")
    print(response.text)

except Exception as e:
    print("\n--- Bir Hata Oluştu ---")
    print(e)