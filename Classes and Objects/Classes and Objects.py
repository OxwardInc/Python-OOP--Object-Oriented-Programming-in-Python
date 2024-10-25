class Person:

    def set_details(self):
        self.name = 'John'
        self.age = 20

    def display(self):
        print('I am a person', self)

    def greet(self):
        print("Hello, how are you doing?", self)

p1 = Person()
p2 = Person()

p1.display()
p2.greet()

p2.display()
p2.greet()