#Inheritence (Kalıtım): Miras alma
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created')
    
    def who_am_i(self):
        print('I am a person')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
    
p1 = Person('Ali','Yolmaz')
s1 = Student('Necmi','Dolmaz', 1461)
t1 = Teacher('Serkan', 'Kolmaz', 'Math')

print(p1.firstname)
print(s1.studentNumber)

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()