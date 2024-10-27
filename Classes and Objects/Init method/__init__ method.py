class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name)

    def greet(self):
        if self.age < 80:
            print("Hello, how are you doing?")
        else:
            print('Hello, how do you do?')
        self.display()

p1 = Person('John', 20)
p1.display()
p1.greet()

p2 = Person('Jack', 90)
p2.display()
p2.greet()


