sayı = int(input("Sayı giriniz: ")) # Kullanıcıdan girdi alıyoruz

tam_bölenler = [] # İki boş liste oluşturuyoruz
ters_işaret = []

if(sayı > 0): # Girilen sayı pozitif ise
    bölen = 1 
    while sayı >= bölen:
        if(sayı % bölen == 0): # Sayı bölene kalansız böündü ise tam_bölenler listesine ekliyoruz
            tam_bölenler.append(bölen) # Sayı bölene kalansız böündüğü için tam_bölenler listesine ekliyoruz
        bölen += 1 # Sayı bölene kalanlı bölündü ise böleni 1 arttırarak tekrardan deniyoruz
    for i in tam_bölenler:  
        ters_işaret.append(i * - 1) # tam_bölenler listesini -1 ile çarparak ters_işaret listesine ekliyoruz

    tam_bölenler.extend(ters_işaret) # ters_işaret listesini tam_bölenler listesine ekliyoruz

elif(sayı == 0): # Girilen sayı nötür ise
    tam_bölenler.append(0)

else: # Girilen sayı negatif ise
    bölen = -1
    while sayı <= bölen:
        if(sayı % bölen == 0):
            tam_bölenler.append(bölen)
        bölen -= 1
    for i in tam_bölenler:
        ters_işaret.append(i * - 1)

    tam_bölenler.extend(ters_işaret)
print("{} tam bölenleri: {}".format(sayı,tam_bölenler)) # Kullanıcıya sayının tam bölenleri yazdırıyoruz

