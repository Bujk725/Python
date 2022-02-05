def asal_sayı(limit):
    asal_sayılar = list()   # Asal_sayılar adında boş bir liste oluşturuyoruz
    for sayı in range(2, limit+1):   # Limit dahil olmadığı içib bir arttırarak yzıyoruz
        bölündü = False
        bölen = 2
        while(sayı > bölen):   # Sayı, bölenden büyük olana kadar döngü yapılıyor
            if(sayı % bölen == 0): 
                bölündü = True    # Sayı, bölene kalansız bölünürse, bölündü True değeri alacak
            bölen += 1   # Sayı, bölene kalansız bölünmezse, bölen bir arttırarak döngü tekrarlanır
        if(bölündü == False):
            asal_sayılar.append(sayı)  # Sayı asalsa asal_sayılar listesine ekliyoruz
    print(asal_sayılar) 


def asal_mı(sayı):
    for i in range(2, sayı):     # İki'den, sayıya kadar i değeri oluşturuyoruz
        if(sayı % i == 0):       
            return False         # Sayı oluşturduğumuz i değerine kalansız bölünürse False değeri dönüyoruz
        return True              # Sayı oluşturduğumuz i değerine bölünmezse True değeri dönüyoruz


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



