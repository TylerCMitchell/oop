class BankAccount:
    bank_name = "First Hero Bank"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            self.balance -= amount
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum


class User:
    bank_name = "First Hero Bank"

    def __init__(self, name):
        self.name = name
        self.account = {
            'checking': BankAccount(0.01, 0),
            'savings': BankAccount(0.01, 0)
        }

    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type):
        self.account[account_type].withdrawal(amount)
        return self

    def display_user_balance(self, account_type):
        print(f"User: {self.name}")
        self.account[account_type].display_account_info()
        return self


Tyler = User("Tyler")
Michael = User("Michael")
Nick = User("Nick")

Tyler.make_deposit(1000, 'checking')
Tyler.make_deposit(575, 'savings')
Tyler.make_deposit(2100, 'checking')
Tyler.make_withdrawal(1500, 'checking')
Tyler.display_user_balance('checking')
Tyler.display_user_balance('savings')

Michael.make_deposit(2000, 'savings')
Michael.make_deposit(500, 'checking')
Michael.make_withdrawal(200, 'savings')
Michael.make_withdrawal(300, 'checking')
Michael.display_user_balance('checking')
Michael.display_user_balance('savings')

Nick.make_deposit(1500, 'checking')
Nick.make_withdrawal(50, 'checking')
Nick.make_withdrawal(100, 'checking')
Nick.make_withdrawal(1000, 'checking')
Nick.display_user_balance('checking')
