class User:

    bank_name = "First National Dojo"
    # now our method has 2 parameters!

    def __init__(self, name):
        # we assign them accordingly
        self.name = name
        # the account balance is set to $0
        self.account_balance = 0
    # adding the deposit method

    # takes an argument that is the amount of the deposit
    def make_deposit(self, amount):
        # the specific user's account increases by the amount of the value recieved
        self.account_balance += amount

    # withdrawal argument
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    # display user balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


tyler = User("Tyler")
michael = User("Michael")
nick = User("Nick")

tyler.make_deposit(1000)
tyler.make_deposit(575)
tyler.make_deposit(2100)
tyler.make_withdrawal(1500)
tyler.display_user_balance()

michael.make_deposit(2000)
michael.make_deposit(500)
michael.make_withdrawal(200)
michael.make_withdrawal(300)
michael.display_user_balance()

nick.make_deposit(1500)
nick.make_withdrawal(50)
nick.make_withdrawal(100)
nick.make_withdrawal(1000)
nick.display_user_balance()

tyler.transfer_money(nick, 200)
tyler.display_user_balance()
nick.display_user_balance()
