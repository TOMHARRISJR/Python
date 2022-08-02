
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        # your code here

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
        # your code here

    def display_account_info(self):
        self.balance = self.balance
        print(f'Balance :${self.balance}')
        return self
        # your code here

    def yield_interest(self):
        gain = self.balance*self.int_rate
        self.balance += gain
        return self


my_BankAccount = BankAccount(.06, 100)
my_BankAccount2 = BankAccount(.06, 100)

my_BankAccount.display_account_info().deposit(50).deposit(850).deposit(
    5000000).withdraw(8900).yield_interest().display_account_info()
my_BankAccount2.display_account_info().deposit(500).deposit(505).withdraw(
    80).withdraw(102).withdraw(500).withdraw(65).yield_interest().display_account_info()
