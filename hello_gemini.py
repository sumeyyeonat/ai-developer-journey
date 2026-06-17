import os
from google import genai
from dotenv import load_dotenv

# 1. .env dosyasındaki gizli şifreleri yükle
load_dotenv()

# 2. Gemini istemcisini başlat
client = genai.Client()

# 3. Canlı bir sohbet (chat) oturumu başlatıyoruz
# Bu oturum, konuşma geçmişimizi arka planda hafızasında tutacak.
chat = client.chats.create(model="gemini-2.5-flash")

print("🚀 Gemini ile Canlı Sohbet Başladı! (Çıkmak için 'çıkış' yazabilirsin)\n")

while True:
    # Kullanıcıdan (senden) girdi alıyoruz
    user_message = input("Siz: ")

    # Eğer 'çıkış' yazarsan döngüyü bitir
    if user_message.lower() == 'çıkış':
        print("\nSohbet sonlandırıldı. Harika bir konuşmaydı!")
        break

    # Boş mesaj gönderilmesini engelle
    if not user_message.strip():
        continue

    try:
        # Mesajı sohbet oturumuna gönderiyoruz
        response = chat.send_message(user_message)

        # Gemini'nin yanıtını ekrana yazdırıyoruz
        print(f"Gemini: {response.text}\n")

    except Exception as e:
        print(f"\n⚠️ Bir hata oluştu: {e}\n")