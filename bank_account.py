class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = 0
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        # your code here

    def make_withdrawal(self, amount):
        if (self.account_balance - amount <= 0):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self
        # your code here

    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
        # your code here

    def yield_interest(self):
        if (self.account_balance > 0):
            self.account_balance *= self.int_rate
        return self
        # your code here

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.account_balance
        return sum


account1 = BankAccount(0.01, 150)
account2 = BankAccount(0.01, 200)

account1.make_deposit(1000).make_deposit(575).make_deposit(
    2100).make_withdrawal(1500).display_account_info()

account2.make_deposit(1500).make_deposit(100).make_withdrawal(50).make_withdrawal(
    100).make_withdrawal(1000).make_withdrawal(25).display_account_info()

BankAccount.all_balances()
