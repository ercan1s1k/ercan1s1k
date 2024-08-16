import os

def dosya_yolu_kontrol(dosya_adi):
    if not os.path.isfile(dosya_adi):
        raise FileNotFoundError(f"{dosya_adi} dosyası bulunamadı.")
    return dosya_adi

def alintilari_oku(dosya_adi):
    try:
        dosya_yolu_kontrol(dosya_adi)
        with open(dosya_adi, 'r', encoding='utf-8') as file:
            alintilar = file.readlines()
            print("Dosya başarıyla okundu.")
            return alintilar
    except FileNotFoundError as fnf_error:
        print(f"Dosya bulunamadı: {fnf_error}")
    except Exception as e:
        print(f"Dosya okunurken hata oluştu: {e}")
    return []

def alintilari_yazdir(alintilar):
    if not alintilar:
        print("Alıntı bulunamadı.")
        return
    for alinti in alintilar:
        print(alinti.strip())

def readme_guncelle(alinti):
    readme_dosyasi = 'readme.md'
    try:
        with open(readme_dosyasi, 'r', encoding='utf-8') as file:
            icerik = file.read()
        
        start_index = icerik.find('<!-- START_QUOTES -->') + len('<!-- START_QUOTES -->')
        end_index = icerik.find('<!-- END_QUOTES -->')
        
        if start_index == -1 or end_index == -1:
            raise ValueError("readme.md dosyasında gerekli işaretler bulunamadı.")
        
        yeni_icerik = icerik[:start_index] + '\n' + alinti.strip() + '\n' + icerik[end_index:]
        
        with open(readme_dosyasi, 'w', encoding='utf-8') as file:
            file.write(yeni_icerik)
        
        print("readme.md dosyası başarıyla güncellendi.")
    except Exception as e:
        print(f"readme.md dosyası güncellenirken hata oluştu: {e}")

def main():
    dosya_adi = 'alintilar.txt'
    alintilar = alintilari_oku(dosya_adi)
    if alintilar:
        alintilari_yazdir(alintilar)
        readme_guncelle(alintilar[0])  # İlk alıntıyı readme.md dosyasına ekle

if __name__ == "__main__":
    main()
