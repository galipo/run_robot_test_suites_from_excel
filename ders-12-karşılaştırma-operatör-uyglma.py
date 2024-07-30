#1- Girilen 2 sayıdan hangisi büyüktür ?
"""a = int(input('1.sayi:'))
b = int(input('2.sayi:'))
result= a>b
print(f"a:{a} , b:{b}'den büyüktür: {result}")"""

#2-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
"""vize1 = int(input('1.vize:'))
vize2 = int(input('2.vize:'))
final = int(input('final:'))
note = ((vize1 + vize2)*6/10) + final*4/10
gecer = note>=50
print(f'ogrenci gecti:{gecer}')"""

#3-Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#(email: email@sadikturan.com parola:abc123)
email=input('email:')
password=input('password:')

e = (email=='email@sadikturan.com')
p = (password=='abc123')
print(f'email is {e} and password is {p}')