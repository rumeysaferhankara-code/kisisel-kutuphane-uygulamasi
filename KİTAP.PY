"""
-------KİŞİSEL KÜTÜPHANE UYGULAMASI-------
Bu uygulama kullanıcıların okunan ve okunacak kitaplar eklemesini, okunmuş,okunmamış ya da tüm kitapların listelemesini,
durumunu(okundu/okunmadı) güncellemesini ve silmesini sağlayan basit bir konsol uygulamasıdır.

Nasıl çalıştırılır?:python kitap.py
 işlevler:
 1-Kitapları listele
   -Tüm kitaplar
   -Sadece okunmuş kitaplar
   -Sadece okunmamış kitaplar
 2-Yeni kitap ekle (Boş başlık/yazar kabul etmez)
 3-Okundu/okunmadı işaretle 
 4-Kitap sil
 5-Çıkış (Kayıtları dosyaya yazar)
 
"""
import json

def kitapları_yükle():
    """kitaplar.json dosyasından verileri okur"""
    try:
        with open ("kitaplar.json","r",encoding="utf-8")as dosya:
             return json.load(dosya)
    except FileNotFoundError:
        return[]

def kitapları_kaydet(kitaplar):
    """Verileri kitaplar.json dosyasına kaydeder."""
    with open("kitaplar.json", "w", encoding="utf-8") as dosya:
        json.dump(kitaplar, dosya, ensure_ascii=False, indent=2)
    print("Kitaplar başarıyla kaydedildi.")

def menü_göster():
    print("\n--- KÜTÜPHANE YÖNETİM SiSTEMİ ---")
    print("1. Kitapları Listele")
    print("2. Yeni Kitap Ekle")
    print("3. Kitap Durumu Güncelle (Okundu/Okunmadı)")
    print("4. Kitap Sil")
    print("5. Çıkış")

def kitapları_listele(kitaplar):
    if not kitaplar:
        print("\nHenüz kayıtlı kitap yok.")
        return
    print("\n--- LİSTELEME SEÇENEKLERİ ---")
    print("1. Tüm Kitaplar")
    print("2. Sadece Okunmuş Kitaplar")
    print("3. Sadece Okunmamış Kitaplar")
    secim = input("Seçiminiz (1-3): ").strip()

    print("\n--- KİTAP LiSTESİ ---")
    bulundu = False

    for index, kitap in enumerate(kitaplar, start=1):
        # 1: Hepsini goster, 2: Sadece okundu olanlar, 3: Sadece okunmadi olanlar
        if secim == "1":
            print(f"{index}. {kitap['başlık']} - {kitap['yazar']} [{kitap['durum']}]")
            bulundu = True
        elif secim == "2" and kitap["durum"] == "okundu":
            print(f"{index}. {kitap['başlık']} - {kitap['yazar']} [{kitap['durum']}]")
            bulundu = True
        elif secim == "3" and kitap["durum"] == "okunmadı":
            print(f"{index}. {kitap['başlık']} - {kitap['yazar']} [{kitap['durum']}]")
            bulundu = True

    if not bulundu:
        print("Bu filtreye uygun kitap bulunamadı.")

def kitap_ekle(kitaplar):
    başlık = input("Kitap Adı: ").strip()
    if not başlık:
        print("Hata: Kitap adı boş bırakılamaz!")
        return  # Kitap adı boşsa alt satırlara (yazara) geçmeden fonksiyonu durdurur

    yazar = input("Yazar Adı: ").strip()
    if not yazar:
        print("Hata: Yazar adı boş bırakılamaz!")
        return  # Yazar boşsa ekleme yapmadan durdurur

    yeni_kitap = {"başlık": başlık,"yazar": yazar,"durum": "okunmadı"}
    
    kitaplar.append(yeni_kitap)
    kitapları_kaydet(kitaplar)
    print(f"'{başlık}' başarıyla eklendi.")

def durum_degistir(kitaplar):
    if not kitaplar:
        print("\nGüncellenecek kitap yok.")
        return
    
    kitapları_listele(kitaplar)
    try:
        sira = int(input("\nDurumunu degiştirmek istediginiz kitabın numarasını girin: "))
        if 1 <= sira <= len(kitaplar):
            seçilen_kitap = kitaplar[sira - 1]
            if seçilen_kitap["durum"] == "okunmadı":
                seçilen_kitap["durum"] = "okundu"
            else:
                seçilen_kitap["durum"] = "okunmadı"
            
            kitapları_kaydet(kitaplar)
            print(f"'{seçilen_kitap['başlık']}' kitabının durumu '{seçilen_kitap['durum']}' olarak güncellendi.")
        else:
            print("Geçersiz kitap numarası!")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")

def kitap_sil(kitaplar):
    if not kitaplar:
        print("\nSilinecek kitap yok.")
        return

    kitapları_listele(kitaplar)
    try:
        sıra = int(input("\nSilmek istediğiniz kitabın numarasını girin: "))
        if 1 <= sıra <= len(kitaplar):
            silinen = kitaplar.pop(sıra - 1)
            kitapları_kaydet(kitaplar)
            print(f"'{silinen['başlık']}' başarıyla silindi.")
        else:
            print("Geçersiz kitap numarası!")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")


kitaplar = kitapları_yükle()

while True:
    menü_göster()
    seçim = input("Seçiminiz (1-5): ").strip()

    if seçim == "1":
        kitapları_listele(kitaplar)
    elif seçim == "2":
        kitap_ekle(kitaplar)
    elif seçim == "3":
        durum_degistir(kitaplar)
    elif seçim == "4":
        kitap_sil(kitaplar)
    elif seçim == "5":
        print("Uygulamadan çıkılıyor. İyi günler!")
        break
    else:
        print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")