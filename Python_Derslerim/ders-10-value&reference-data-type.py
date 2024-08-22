#Value veri tipi#
a = 5 
b = 10

a = b

b = 15

print(a)

#b yi değiştirmemize rağmen b nin son değeri yerine atanan değeri terminale bastırır. Çünkü value veri tipinde değişkenlere değer atanır.

#Reference veri tipi#

x = [1,2,3]
y = [4,5,6]

x = y

y[0]= 8

print(x)

#y' yi x'e eşitlediğimizde ve daha sonrasında y' de değişiklik yaptığımızda aynı değişiklikler x'te de oluyor.
# Çünkü list veri tipinde (reference) list değişkenlerine değer değil adres atanır. Yani x=y yaptığımızda adresleri eşitlemiş oluyoruz.
