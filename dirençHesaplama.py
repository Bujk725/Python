print("4 veya 5 Bandlı Direnç Renklerine Göre Ω Hesaplama Programına Hoşgeldiniz")

def RenkKodları(*değer):  # args kullanarak 1 den fazla değer alabiliyoruz
    renkler = ["siyah","kahverengi","kırmızı","turuncu","sarı","yeşil","mavi","mor","gri","beyaz","altın","gümüş"]
    boş = []
    for i in değer: 
        boş.append(renkler.index(i)) #  Renklerin index sayılarını boş listesine ekliyoruz
    if(len(boş) == 4): #  4 tane renk girilir ise burası çalışacak
        if(boş[3] == 10): #  Tolerans değeri altın ise 
            sonuç = (boş[0] * 10 + boş[1]) * 10 ** boş[2] 
            print("{}Ω %5".format(sonuç))
        elif(boş[3] == 11): # Tolerans değeri gümüş ise
            sonuç = (boş[0] * 10 + boş[1]) * 10 ** boş[2]
            print("{}Ω %10".format(sonuç)) 



    elif(len(boş) == 5): #  5 tane renk girilir ise burası çalışacak
        if(boş[4] == 10): #  Tolerans değeri altın ise 
            sonuç = (boş[0] * 100 + boş[1] * 10 + boş[2]) * 10 ** boş[3] 
            print("{}Ω %5".format(sonuç))
        elif(boş[4] == 11): # Tolerans değeri gümüş ise
            sonuç = (boş[0] * 100 + boş[1] * 10 + boş[2]) * 10 ** boş[3] 
            print("{}Ω %10".format(sonuç)) 
    

direnç = int(input("Dirençdeki renk sayısı kaçtır? :")) #  Kullanıcıdan input alıyoruz


try: 
    if(direnç == 4):
        ilk = input("İlk renk nedir? :")
        ikinci = input("İkinci renk nedir? :")
        üçüncü = input("Üçüncü renk nedir? :")
        dördüncü = input("Dördüncü renk nedir? :")
        RenkKodları(ilk,ikinci,üçüncü,dördüncü)
    elif(direnç == 5):
        ilk = input("İlk renk nedir? :")
        ikinci = input("İkinci renk nedir? :")
        üçüncü = input("Üçüncü renk nedir? :")
        dördüncü = input("Dördüncü renk nedir? :")
        beşinci = input("Beşinci renk nedir? :")
        RenkKodları(ilk,ikinci,üçüncü,dördüncü,beşinci)
    else:
        print("4 veya 5 renk sayısını desteklemektedir!")
except ValueError: #  Kullanıcı yanlış renk ismi girerse uyarı veriyoruz
    print("Lütfen renk isimlerinin adını tam ve küçük half de yazınız!")
