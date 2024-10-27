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



class BankAccount:

    rate_of_interest = 5 # class variable
    minimum_balance = 100 # class variable
    minimum_balance_fees = 10 # class variable

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount('7348', 'Tom', 50)
account2 = BankAccount('6378', 'Bob', 400)




class Book:

    x = 5

    def __init__(self):
        self.x = 100

    def display(self):
        print(self.x)

b = Book()
b.display()


class Account:

    rate = 5

    def some_method(self):
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        self.rate = 10
        Account.rate = 10
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))

a1 = Account()
a2 = Account()