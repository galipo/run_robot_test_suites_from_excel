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
    
# object(instance)

p1= Person("ali",1990)     #veya p1=Person(name="ali", year=1990) olarak tanımlayabilirsin.
p2= Person("ece",2000)

#accesing object attributes
print(f'p1= name: {p1.name} year: {p1.year} adress: {p1.address}')
print(f'p2= name: {p2.name} year: {p2.year}')

#updating
p1.name='necmi'
p1.address='İzmit'

#accesing object attributes
print(f'p1= name: {p1.name} year: {p1.year} adress: {p1.address}')

print(p1)
print(p2)

print(type(p1))
print(type(p2))

a = (p1==p2)
print(a)