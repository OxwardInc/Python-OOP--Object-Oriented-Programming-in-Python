class MyClass():
    a = 5

    def __init__(self, x):
        self._x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)


MyClass.method2()



class Person:

    species = 'Homo Sapiens' # Class variable
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    def display(self):
        print(f"{self.name} is{self.age} years old.")

    @classmethod
    def show_count(cls):
        print(f"There are {cls.count} {cls.species}")

    

Person.show_count()

p1 = Person('Jack', 20)
p2 = Person('Jhon', 34)

p1.display()
p2.display()



from employee import Employee
from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"I'm {self.name}, {self.age} years old")

    @classmethod
    def from_str(cls, s):
        name, age = s.split(', ')
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])

    @classmethod
    def from_employee(cla, emp):
        name = emp.first_name + ' ' + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cla(name, age)

p1 = Person('John', 20)
p2 = Person('Jack', 34)

s = 'Jim 23'
p3 = Person.from_str(s)
p3.display()

d = {'name': 'Jane', 'age': 34}
p4 = Person.from_dict(d)
p4.display()

e1 = Employee("james", "Smith", 1990, 6000)
p5 = Person.from_employee(e1)
p5.display()
