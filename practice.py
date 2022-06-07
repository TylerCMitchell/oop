class User:
    bank_name = "First National Dojo"
    # now our method has 2 parameters!

    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
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
        return self

    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
# guido.bank_name = "Dojo Credit Union"
#User.bank_name = "Bank of Dojo"
# print(guido.bank_name)  # output: Dojo Credit Union
# print(monty.bank_name)
#guido.name = "Guido"

###### - ALL ABOVE CODE TESTED AND WORKS - ######

"""
print(guido.name)  # output: Guido - Tested and it works
#monty.name = "Monty"
print(monty.name)  # output: Monty - " "
"""
###### - These work - #########

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
"""
print(guido.account_balance)  # output: 300 - Tested and it works
print(monty.account_balance)  # output: 50 - " "
"""
guido.make_withdrawal(25)
monty.make_withdrawal(15)
"""
print(guido.account_balance)
print(monty.account_balance)
"""
### - These work - ###
# guido.display_user_balance()
# monty.display_user_balance()

guido.transfer_money(monty, 75)
print(guido.account_balance)
print(monty.account_balance)
