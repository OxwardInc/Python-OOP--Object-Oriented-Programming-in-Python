class Account:

    rate = 5

    def some_method(self):
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        self.rate = 10
        Account.rate = 10
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))

a1 = Account()
a2 = Account()