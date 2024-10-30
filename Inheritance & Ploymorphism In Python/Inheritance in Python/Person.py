class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age}")

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}")