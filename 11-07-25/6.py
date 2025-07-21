class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance)


acc = BankAccount()
acc.deposit(1000)
acc.withdraw(200)
acc.display_balance()
