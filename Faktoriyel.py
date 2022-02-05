def Faktoriyel(sayı):
    çarpım = 1
    while sayı>1:
        çarpım *= sayı # Girilen sayıyı çarpım ile çarpıp, çarpıma eşitliyoruz
        sayı -= 1 # Sayıyı bir azaltıyoruz
    print(çarpım)



print("Faktoriyel Uygulaması")
    

while True:

    sayı = input("Sayı giriniz(Çıkmak için 'q' ya basınız!):") # Kullanıcıdan sayı alıyoruz
    
    if(sayı == "q"): # Eğer kullanıcı q'ya basarsa döngü sonlandırılıyor.
        print("Programdan çıkılıyor....")
        break
    elif(sayı >= "0"): # Girilen sayı negatif sayı değilse fonksiyon çalıştırıyoruz
        sayı = int(sayı) # İnput ile girilen sayıyı tam sayıya çeviriyoruz
        Faktoriyel(sayı)
    else: 
        print("Lütfen pozitif sayı giriniz:")

    