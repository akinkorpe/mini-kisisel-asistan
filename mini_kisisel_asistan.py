# Kullanıcıdan temel bilgileri alalım
ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
dogum_yili = int(input("Doğum yılınızı giriniz: "))
sehir = input("Yaşadığınız şehir: ")

# Mevcut yıl
suanki_yil = 2025
yas = suanki_yil - dogum_yili

# Yaş kategorisi
if yas <= 11:
    kategori = "Çocuk"
elif 12 <= yas <= 17:
    kategori = "Genç"
else:
    kategori = "Yetişkin"

# Bilgi özeti
print("-" * 30)
print(f"Merhaba {ad} {soyad}!")
print(f"{yas} yaşındasınız ve {kategori} kategorisindesiniz.")
print(f"{sehir} şehrinde yaşıyorsunuz.")
print("-" * 30)

# Ekstra işlemler
print("\nİsim bilgisi üzerine bazı işlemler yapılacak:")

ters_ad = ad[::-1]
buyuk_ad = ad.upper()
uzunluk = len(ad + soyad)

print(f"İsminizin tersten yazımı: {ters_ad}")
print(f"İsminizin büyük harflerle yazımı: {buyuk_ad}")
print(f"Ad + Soyad uzunluğunuz (karakter sayısı): {uzunluk}")

print("\nİsteğe bağlı işlemler:")
print("1 - İsmini tersten yaz")
print("2 - İsmini büyük harfle yaz")
print("3 - İsim uzunluğunu hesapla")
print("4 - Hepsini yap")

secim = input("Bir işlem seçiniz (1/2/3/4): ")

if secim == "1":
    print(f"Ters isim: {ad[::-1]}")
elif secim == "2":
    print(f"Büyük harfle: {ad.upper()}")
elif secim == "3":
    print(f"Uzunluk: {len(ad + soyad)} karakter")
elif secim == "4":
    print(f"Ters: {ad[::-1]}")
    print(f"Büyük: {ad.upper()}")
    print(f"Uzunluk: {len(ad + soyad)}")
else:
    print("Geçersiz seçim yapıldı.")