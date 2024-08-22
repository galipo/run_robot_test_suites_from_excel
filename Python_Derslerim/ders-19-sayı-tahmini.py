"""
1-100 arasinda rastgele üretilecek bir sayiyi aşaği yukari ifadeleri ile
buldurmaya çalişin. (hak 5)
** "random modülü” için ”python random” şeklinde arama yapin.
** 100 üzerinden puanlama yapin. Her soru 20 puan.
** hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi
üzerinden hesaplansin
"""
num = list(range(1,100))
import random 
num = int(random.choice(num))

hak = int(input("kaç tahminde bulunacaksiniz: "))
tahmin = 0
puan=100
eksilme = puan/hak

while hak!=0:
    tahmin = int(input("sayiyi tahmin ediniz:" ))
    if tahmin == num:
        print(f'TEBRİKLER DOĞRU BİLDİNİZ! SAYİ={num}. Puaniniz={puan}')
        hak = 0
        continue
    elif tahmin>num:
        print('Daha KÜÇÜK bir sayi.')   
    elif tahmin<num:
        print('Daha BÜYÜK bir sayi.')       
    hak = hak-1
    puan = puan-eksilme

if tahmin!=num:
    print(f"BİLEMEDİN MAL! SAYI {num}'di. Puanin={puan}")