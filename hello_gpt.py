import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. .env dosyasındaki gizli şifreleri hafızaya yükle
load_dotenv()

# 2. OpenAI istemcisini (client) başlat
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("GPT-4o'ya mesaj gönderiliyor...")

try:
    # 3. GPT-4o modeline ilk mesajımızı gönderiyoruz
    response = client.chat.completions.create(
        model="gpt-4o",  # OpenAI'ın en güncel ve güçlü amiral gemisi modeli
        messages=[
            {"role": "user", "content": "Merhaba GPT-4o! Ben 60 günlük bir yapay zeka öğrenme yolculuğuna başladım. Bana bu yolculuk için tek cümlelik harika bir tavsiye verir misin?"}
        ],
        max_tokens=100
    )

    # 4. Gelen cevabı ekrana yazdırıyoruz
    print("\n--- GPT-4o'nun Cevabı ---")
    print(response.choices[0].message.content)

except Exception as e:
    print("\n--- Bir Hata Oluştu ---")
    print(e)