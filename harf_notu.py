def hesaplama(vize,final):
    ortalama = (vize * 4 /10) + (final * 6/10) # Girilen puanların ortalamasını alıyoruz
    if(ortalama >= 90):  # Ortalamamızın şartını yazıyoruz
        return "AA" # Şartı sağlayan değeri döndürüyoruz
    elif(ortalama >= 85):
        return "BA"
    elif(ortalama >= 80):
        return "BB"
    elif(ortalama >= 75):
        return "CB"
    elif(ortalama >= 70):
        return "CC"
    elif(ortalama >= 65):
        return "DC"
    elif(ortalama >= 60):
        return "DD"
    else:   # Yukardaki koşullar sağlanmadığında sağlanan koşul
        return "FF"


print("--------------------Harf Notu Hesaplama Uygulamasına Hoşgeldiniz--------------------")

vize = int(input("Vize1 Notunuzu Giriniz: ")) # İnput string değerinde çıktı verdiği için integer'a çeviriyoruz
final = int(input("Final Notunuzu Giriniz: ")) # İnput string değerinde çıktı verdiği için integer'a çeviriyoruz
print("Ortalamanız:",format(hesaplama(vize,final)))
