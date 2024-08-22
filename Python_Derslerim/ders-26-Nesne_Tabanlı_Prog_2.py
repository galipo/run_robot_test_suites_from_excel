# Object Oriented Programming (OOP)

# class
class Person:
    

     #class attributes
     address = 'no information'

     #constructor(yapıcı metod)
     def __init__(self,names,years):

        #object attributes
        self.name=names
        self.year=years
        print('init metodu basladi')
     
    #instance methods
     def intro(self):
      print('Hello there.I am ' + self.name)

     def calculateAge(self):
        return 2024-self.year


# object(instance)

"""
p1= Person("Ali",1990)     #veya p1=Person(name="ali", year=1990) olarak tanımlayabilirsin.
p2= Person("Ece",2000)

p1.intro()
p2.intro()

print(f"{p1.name}'nin yaşi: {p1.calculateAge()} ")
"""

class Circle:
   #class object attribute
   pi=3.14

   def __init__(self, yaricap=1):
      self.yaricap = yaricap

   #Methods
   def cevre_hesapla(self):
      return 2*self.pi*self.yaricap
   
   def alan_hesaplama(self):
      return self.pi * (self.yaricap**2)
   
c1=Circle()
c2=Circle(5)

print(f'c1 : alan = {c1.alan_hesaplama()} cevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesaplama()} cevre = {c2.cevre_hesapla()}')