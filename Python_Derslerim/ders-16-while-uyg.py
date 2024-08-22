#1'den 100'e kadar yazdırma:
"""x= 1
while x<=100:
    print(x)
    x+=1
print('bitti')"""

#Örnek uygulama#
sayilar=[1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
"""n=0
while n<=7:
    print(sayilar[n])
    n=n+1"""

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
"""x=int(input('please enter a first number: '))
y=int(input('please enter a last number: '))
while x<=y:
    if x%2==0:
        print(f"{x} çifttir.")
    else:
        print(f"{x} tektir.")       
    x=x+1"""

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""x= 100
while x>0:
    print(x)
    x-=1
print('bitti')"""

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
"""s1=int(input('lütfen 1. sayiyi giriniz: '))
s2=int(input('lütfen 2. sayiyi giriniz: '))
s3=int(input('lütfen 3. sayiyi giriniz: '))
s4=int(input('lütfen 4. sayiyi giriniz: '))
s5=int(input('lütfen 5. sayiyi giriniz: '))
numbers = [s1,s2,s3,s4,s5]
n=0
while n<=4:
    print(numbers[n])
    n=n+1"""

#5:Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#   ürün sayısını kullanıcıya sorun.
#   dictionary listesi yapısı (name, price) şeklinde olsun.
#   ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
cesit = int(input("gireceginiz ürün cesit sayisi: "))
i=0
mal = []
while i<cesit:
    ürün = input("ürün adi giriniz: ")
    fiyat = input("ürün fiyati giriniz: ")
    adet = input("ürün stok adeti giriniz: ")
    
    mal.append({ 'ürün': ürün,
                 'fiyat': fiyat,
                 'adet': adet  })
    i+=1
for urun in mal:
    print(f'ürün adi: {mal["ürün"]}\nürün fiyati: {mal["fiyat"]}\nürün stok adeti: {mal["adet"]}')