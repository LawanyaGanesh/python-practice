class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        print("Available Amount:", self.balance)


bank1 = BankAccount(1000)

bank1.deposit(500)
bank1.get_balance()