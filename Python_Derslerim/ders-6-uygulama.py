website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 'Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
"""message = ' Hello World '
message = message.split()
message = ' '.join(message)
print(message)"""

#2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
"""result = website.replace('http://www.sadikturan.com','www.sadikturan.com')
print(result)"""

#3 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
"""course = course.lower()
print(course)"""

#4 'website' içinde kaç tane a karakteri vardır ? (count('a'))
"""result = website.count('a')
print(result)"""

#5 'website' "www” ile başlayıp "com" ile bitiyor mu?
"""result1 = website.startswith('www')
result2 = website.endswith('com')
print(result1,result2)"""

#6 'website' içinde '.com' ifadesi var mı?
"""right = website.find('.com')
print(right)"""

#7 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
"""right = course.isalpha()
print(right)"""

#8 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
"""text = 'Contents'
text = text.center(50,'*')
print(text)"""

#9 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
"""course = course.replace(' ','-')
print(course)"""

#10 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
"""text = 'Hello World'
text = text.replace('World','There')
print(text)"""

#11 'course' karakter dizisini boşluk karakterlerinden ayırın.
"""course = course.split()
print(course)"""