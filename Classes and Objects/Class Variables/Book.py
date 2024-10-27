class Book:

    x = 5

    def __init__(self):
        self.x = 100

    def display(self):
        print(self.x)

b = Book()
b.display()