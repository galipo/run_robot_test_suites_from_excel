website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

#1 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))     #65

#2 'website' içinden www karakterlerini alın.
print(website[7:10])

#3 'website' içinden com karakterlerini alın.
print(website[22:25])
#4 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[0:15] + ' ' + course[10:])
#5 'course' ifadesindeki karakterleri tersten yazdırın.
new =course[::-1]
print(new)