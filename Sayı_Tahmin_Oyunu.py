import random 
import time
# Kütüphaneyi ekliyoruz

print("Sayı Oyunumuza Hoşgeldiniz")
sayı = random.randint(0,101) # 0 ile 100 arasında rastgele sayı oluşturuyoruz
hak = 5 # Kullanıcıya hak veriyoruz
yaklaşma = random.randint(1,6) # 1 ile 5 arasında yaklaşma değişkeni oluşturuyoruz
while True: # Sonsuz döngümüzü oluşturduk
    
    if(hak == 0): # Kullanıcının hakkı bitince döngü sonlanıyor
        print("Kaybettiniz!")
        break

    tahmin = int(input("Sayınızı Giriniz: ")) # Kullanıcıdan tahmin alıyoruz
    
    if(abs(sayı-tahmin) > yaklaşma or yaklaşma > abs(sayı-tahmin)): # Tahmin sayıya, yaklaşma kadar yakınsa, kullanıcıya Yaklaştınız yazıyoruz
        print("Yaklaştınız")

    if(tahmin > sayı): # Tahmin sayıdan büyükse 
        print("Düşünülüyor (＠_＠;)")
        time.sleep(2) # İki saniye bekliyoruz
        hak -= 1 # Hakkı bir azaltıyoruz
        print("Tahmininiz sayıdan büyüktür!\n Hakkınız: {} kalmıştır".format(hak)) 
    elif(tahmin< sayı): # Tahmin sayıdan küçükse
        print("Düşünülüyor (＠_＠;)")
        time.sleep(2)
        hak -= 1
        print("Tahmininiz sayıdan küçüktür!\n Hakkınız: {} kalmıştır".format(hak))
    
    else: # Doğru bilirse
        print("Düşünülüyor (＠_＠;)")
        time.sleep(2)
        hak -= 1
        print("Tebrikler Bildiniz (¬‿¬)")
        break
