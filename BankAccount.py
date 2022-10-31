class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Your balance is ${self.balance:.2f}.")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        censored_account_number = (
            "*" * (len(str(self.account_number)) - 4) + str(self.account_number)[-4:]
        )
        print(
            f"\n{self.full_name}\nAccount No.: {censored_account_number}\nBalance: ${self.balance:.2f}\n"
        )

huey = BankAccount("Hubert Duck", 1029384756)
dewey = BankAccount("Dewford Dingus Duck", 1874609235)
louie = BankAccount("Llewellyn Duck", 1627384509)

huey.deposit(400000)
huey.print_statement()
huey.add_interest()
huey.print_statement()
huey.withdraw(150)
huey.print_statement()

print('===========\n')

dewey.deposit(400)
dewey.print_statement()
dewey.add_interest()
dewey.print_statement()
dewey.withdraw(350)
dewey.print_statement()
dewey.withdraw(150)
dewey.print_statement()

print('===========\n')

louie.deposit(1000)
louie.print_statement()
louie.add_interest()
louie.get_balance()
louie.withdraw(50.83)
louie.print_statement()
