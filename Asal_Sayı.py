def asal_sayı(limit):
    asal_sayılar = list()
    for sayı in range(2, limit+1):
        bölündü = False
        bölen = 2
        while(sayı > bölen):
            if(sayı % bölen == 0):
                bölündü = True
            bölen += 1
        if(bölündü == False):
            asal_sayılar.append(sayı)
    print(asal_sayılar)


def asal_mı(sayı):
    for i in range(2, sayı):
        if(sayı % i == 0):
            return False
        return True


print("""

Asal Sayı Programı

Seçenekler;

1- 2' den girdiğiniz sayıya kadar olan asal sayıları gösterir.

2- Girdiğiniz sayının asal olup olmadığını gösterir.

""")

işlem = input("Seçenek seçiniz: ")
if(işlem == "1"):
    sayı = int(input("Üst Sınır giriniz: "))
    if(sayı > 1):
        asal_sayı(sayı)
    else:
        print("Lütfen bir den büyük sayı giriniz!")
elif(işlem == "2"):
    sayı = int(input("Sayı giriniz: "))
    if(sayı> 1):
        if(asal_mı(sayı)):
            print("{} asaldır".format(sayı))
        else:
            print("{} asal değildir".format(sayı))
    else:
        print("Bir den büyük sayı giriniz!")



