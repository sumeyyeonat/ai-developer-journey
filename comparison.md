# 🤖 4. Gün: Claude vs GPT-4o Karşılaştırması

## 1. Kod Yapısı (Syntax) Farkları
- **Anthropic (Claude):** İstemciyi başlatırken `Anthropic()` kullandık ve mesaj oluştururken `client.messages.create` yapısını tercih ettik. Model adı olarak `claude-3-5-sonnet-20241022` verdik.
- **OpenAI (GPT):** İstemci için `OpenAI()` kullandık ve mesaj oluştururken `client.chat.completions.create` yapısını tercih ettik. Model adı olarak `gpt-4o` verdik.

## 2. Alınan Sonuçlar ve Çıktılar
- **Claude API Sonucu:** Hesaptaki bakiye (kredi) yetersizliği nedeniyle `400 BadRequestError` hatası alındı.
- **GPT-4o API Sonucu: "Bakiye hatası alındı"

## 3. Benim Değerlendirmem
İki büyük yapay zeka şirketinin de kütüphane mantığı birbirine çok benziyor. İkisi de güvenlik için `.env` dosyasından şifre okuyor.

## 4. Google Gemini Deneyimi (Ücretsiz Kurtarıcı)
- **Sonuç:** OpenAI ve Anthropic bakiye hatası verirken, Google Gemini API ücretsiz katmanı sayesinde kredi kartı istemeden `gemini-2.5-flash` modeliyle bize canlı yanıtı başarıyla döndürdü. Öğrenme sürecimize bütçe dostu olarak Gemini ile devam edebiliriz!