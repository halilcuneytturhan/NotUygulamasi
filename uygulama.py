# NOT UYGULAMASI

# 1 - Menu
    # 1 - Not gir.
    # 2- Ortalamaları göster.
    # 3 - Notları kayıt et
    # 4 - Çıkış

def not_hesapla(satir):
    if not satir.strip():
        return "Boş satır\n"
    
    satir = satir.strip()
    liste = satir.split(":")
    if len(liste) < 2: 
        return "Hatalı format: 'Ad Soyad:Not1,Not2,Not3' olmalı\n"
    
    ogrenciAdi = liste[0]
    try:
        notlar = liste[1].split(",")
        if len(notlar) != 3:
            return f"{ogrenciAdi} : Eksik not bilgisi\n"
        
        not1 = int(notlar[0])
        not2 = int(notlar[1])
        not3 = int(notlar[2])
    except ValueError:
        return f"{ogrenciAdi} : Not bilgisi sayısal değil\n"

    ortalama = (not1 + not2 + not3) / 3
    if 90 <= ortalama <= 100:
        harf = "AA"
    elif 80 <= ortalama < 90:
        harf = "BA"
    elif 70 <= ortalama < 80:
        harf = "BB"
    elif 60 <= ortalama < 70:
        harf = "CB"
    elif 50 <= ortalama < 60:
        harf = "CC"
    else:
        harf = "FF"
    
    return f"{ogrenciAdi} : {harf} - ( {ortalama:.2f} )\n"


def not_gir():
    ad = input("Öğrenci adi :")
    soyad = input("Öğrenci soyad :")
    not1 = input("Not 1 :")
    not2 = input("Not 2 :")
    not3 = input("Not 3 :")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+' : '+not1+' , '+not2+' , '+not3+ '\n')


def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for i in file:
            sonuc = not_hesapla(i)
            print(sonuc)

def notlari_kaydet():
    with open("sinav_notlari.txt" , "r", encoding= "utf-8") as file:
        liste = []

        for satir in file:
            sonuc = not_hesapla(satir)
            if sonuc.strip():
                liste.append(sonuc)        
            
        with open("sonuclar.txt", "w" , encoding= 'utf-8' ) as file2:
            file2.writelines(liste)

while True:
    islem = input("1-Not Gir\n2-Notları oku\n3-Notları kayıt et\n4-Çıkış\nSeçim: ")

    if (islem=='1'):
        not_gir()
    elif (islem=='2'):
        notlari_oku()    
    elif(islem=='3'):
        notlari_kaydet()
    else:
        break