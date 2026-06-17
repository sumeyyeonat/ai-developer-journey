import os
from anthropic import Anthropic
from dotenv import load_dotenv

# 1. .env dosyasındaki gizli şifreleri bilgisayarın hafızasına yükle
load_dotenv()

# 2. Anthropic istemcisini (client) başlat. Şifreyi otomatik olarak hafızadan çeker.
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

print("Claude'a mesaj gönderiliyor...")

# 3. Claude'a ilk mesajımızı gönderiyoruz
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",  # Kullanacağımız güçlü Claude modeli
    max_tokens=1000,                     # Cevabın maksimum uzunluğu
    messages=[
        {"role": "user", "content": "Merhaba Claude! Ben 60 günlük bir yapay zeka öğrenme yolculuğuna başladım. Bu bizim seninle ilk kodlu iletişimimiz. Bana kısa bir motivasyon cümlesi söyler misin?"}
    ]
)

# 4. Claude'dan gelen cevabı ekrana yazdırıyoruz
print("\n--- Claude'un Cevabı ---")
print(message.content[0].text)