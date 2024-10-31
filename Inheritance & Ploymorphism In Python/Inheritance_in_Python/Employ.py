from Person import Person

class Employee(Person):
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        Person.__init__(self, name, age, address, phone)
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    def contact_details(self):
        super().contact_details()
        print(f"Office Address: {self.office_address}, Office Phone: {self.office_phone}")

emp = Employee('jack', 30, 'D4, XYZ street, Delhi', '994477291', 8000, 'ABC Street, Delhi', '897865589')
