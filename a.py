# Dosya adını değiştirin veya yolunu belirtin
dosya_adı = "C:\\Users\\batuh\\Desktop\\Yeni klasör (7)\\b.txt"

try:
    # Dosyayı oku ve içeriğini al
    with open(dosya_adı, "r", encoding="utf-8") as dosya:
        içerik = dosya.read()

    # Tüm harfleri sil
    temiz_icerik = ''.join(char for char in içerik if not char.isalpha())

    # Dosyayı yeniden yaz ve temiz içeriği yaz
    with open(dosya_adı, "w", encoding="utf-8") as dosya:
        dosya.write(temiz_icerik)

    print("Tüm harfler başarıyla silindi.")

except FileNotFoundError:
    print("Belirtilen dosya bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)