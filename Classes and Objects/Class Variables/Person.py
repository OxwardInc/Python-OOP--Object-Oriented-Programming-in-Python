class Person:

    species = 'Homo Sapiens' # Class variable
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    def display(self):
        print(f"{self.name} is{self.age} years old. {Person.species}")
        print(f'{Person.count}')

    
p1 = Person('Jack', 20)
p2 = Person('Jhon', 34)

p1.display()
p2.display()