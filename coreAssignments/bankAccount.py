class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds!")
            return self
        self.balance = self.balance-amount
        print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance*self.int_rate)
        return self


my_bankAccount = BankAccount(0.01, 100)
my_bankAccount2 = BankAccount(0.01, 100)


my_bankAccount.display_account_info().deposit(5).withdraw(50).deposit(
    200).deposit(50).yield_interest().display_account_info()
my_bankAccount2.display_account_info().deposit(5).withdraw(50).deposit(
    200).withdraw(10).withdraw(60).withdraw(50).yield_interest().display_account_info()
