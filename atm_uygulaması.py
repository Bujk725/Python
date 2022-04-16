import time
print("""

ATM Uygulamasına Hoşgeldiniz

İşleminizi Seçiniz:

1) Bakiye Sorgula

2) Para Çek

3) Para Yatır

4) Çıkış Yap
""")
bakiye = 100
while(True):
    işlem = input("İşleminizi Yazınız: ")
    if(işlem == "4"):
        print("Programdan Çıkılıyor")
        time.sleep(1)
        print("Programdan Çıkıldı")
        break

    elif(işlem == "1"):
        print("Paranız sayılıyor")
        time.sleep(1.5)
        print("Bakiyeniz: {}TL dir".format(bakiye))

    elif(işlem == "2"):
        çekme = int(input("Miktar Giriniz: "))
        if(çekme > bakiye ):
            print("Bu miktarda para çekemezsiniz. Hesabınızda {}TL bulunuyor".format(bakiye))
            time.sleep(1)
            cevap = input("Tekrar tuşuna veya İptal tuşuna basınız: ")
            if(cevap == "Tekrar"):
                continue
            else:
                print("İşlem iptal edimiştir. Programdan çıkılıyor")
                time.sleep(1)
                print("Programdan çıkılmıştır")
                break
        print("Parayı hazneden alınız")    
        time.sleep(1)
        bakiye -= çekme
        print("Bakiyeniz: {}TL dir".format(bakiye))

    elif(işlem == "3"):
        yatırma = int(input("Miktar Giriniz: "))
        print("Parayı hazneye koyunuz")
        time.sleep(2)
        cevap = input("Devam veya İptal tuşuna basınız: ")
        if(cevap == "İptal"):
            print("İşlem iptal edimiştir. Paranızı geri alınız\nProgramdan çıkılıyor")
            time.sleep(1)
            print("Programdan çıkılmıştır")
            break
        print("Paranız sayılıyor")
        time.sleep(1.5)
        bakiye += yatırma
        print("Bakiyeniz: {}TL dir".format(bakiye))
            

