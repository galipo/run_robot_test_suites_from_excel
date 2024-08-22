#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

"""def againer(word, time):
    i = 1 
    while i<=time:
        print(word*time)
        i=i+1

againer('Fatih', 6)"""

#2-Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren bir fonksiyon yazın.

"""def turnlist(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste

turnlist(10,20,30,'Merhaba')"""

#3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
#çalışmıyor!!!!!!!!!!!
"""def asal(num1,num2):
    i=1
    list = [1]
    while num1<=num2:
        while i<=num1:
            if (num1%i)!=0:
                list.append(num1)
            i=i+1
        num1=num1+1
    print(list)
num1 =int(input("please enter a number: "))
num2 =int(input("please enter a number: "))
asal(num1,num2)"""

#4- Kendisine gönderilen bir tam sayının bölenleriyle liste oluşturan bir fonk. yazınız.

"""def tambol(num):
    i = 1
    list =[]
    while i<=num:
        if num % i == 0:
            list.append(i)
        i=i+1
    print(list)

num1=int(input("please enter a nmber: "))
tambol(num1)"""