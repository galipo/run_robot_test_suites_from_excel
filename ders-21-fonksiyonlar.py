#Basit bir fonksiyon
"""
def printhello(name):
    print("hello " + name)

printhello('Selami')"""

def retired(name, year):
    "Ememklilik yasini hesaplar. İlk basta isim sonrasinda yil giriniz."
    age= 2024 - year
    ret = 86-age
    print(f'{name} emeklilik yasiniz {ret}')

help(retired)
retired('Fatih', 2001)    
