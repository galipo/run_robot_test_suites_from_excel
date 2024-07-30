"""numbers = [1,2,3,4,5]       #List için for loop#
for num in numbers:
    print(num)

names=['ali','mehmet','fuat','necmi']
for name in names:
    print(name)

box = [(1,2),(3,4),(5,6)]
for x,y in box:
    print(x,y)
    print(x)
    print(y)"""


"""name = 'Fatih Topal'        #String için for loop#
for n in name:
    print(n)"""

"""tuple = (1,2,3,4,5)         #Tuple için for loop#
for t in tuple:
    print(t)"""

"""d = {'k1':1,'k2':2,'k3':3}  #Dictionary için for loop#
for key,value in d.items():
    print(key)
    print(value)
    print(key,value)"""

#Örnek Uygulamalar#

sayilar =[1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
"""for n in sayilar:
    if n%3==0:
        print(f"{n}--> 3'e tam bölünür.")
    else:
         print(f"{n}--> 3'e tam bölünmmez.")   """

# 2- Sayilar listesinde sayıların toplamı kaçtır ?
"""sum =0
for n in sayilar:
    sum=sum+n
print(sum)   """ 
# 3- Sayilar listesindeki tek sayıların karesini alınız.
"""for n in sayilar:
    if n%2!=0:
       res= n**2
       print(f"{n} bir tek sayidir ve karesi {res}'dir. ")"""
