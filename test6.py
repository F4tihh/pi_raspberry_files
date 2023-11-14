import os

def create_resim_id_listesi():
    resim_id_listesi = []

    # Resim dosyalarının bulunduğu dizini belirtin
    resim_dizini = "/path/to/your/image/directory"  # Kendi resim dizininizi buraya yazın

    # Dizindeki dosya isimlerini al
    dosya_isimleri = os.listdir(resim_dizini)

    # Dosya isimlerini analiz et ve resim_id_listesi'ne ekle
    for dosya_adi in dosya_isimleri:
        if dosya_adi.startswith("resim_") and dosya_adi.endswith(".jpg"):
            resim_numarasi = dosya_adi.split("_")[1].split(".")[0]  # Örnek: "resim_1.jpg" -> 1
            resim_id_listesi.append(int(resim_numarasi))

    return resim_id_listesi

# Oluşturulan resim_id_listesi'ni kullanarak ana kodu çalıştır
def main():
    resim_id_listesi = create_resim_id_listesi()
    print("Oluşturulan resim_id_listesi:", resim_id_listesi)
    # ... (kalan kod buraya eklenmeli)

if __name__ == "__main__":
    main()