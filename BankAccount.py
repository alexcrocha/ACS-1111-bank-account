class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self):
        print(f"Your balance is ${self.balance}.")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest


alex_account = BankAccount("Alex Rocha", 43536373)

alex_account.deposit(1000)
alex_account.deposit(500)

alex_account.withdraw(1400)
alex_account.withdraw(200)

alex_account.get_balance()
alex_account.add_interest()
alex_account.get_balance()
