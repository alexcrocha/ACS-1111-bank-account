import random


class BankAccount:
    def __init__(self, full_name, balance=0):
        self.full_name = full_name
        self.balance = balance
        self.account_number = self.__account_number_generator()

    def __account_number_generator(self):
        number = [str(random.randint(1, 9))]
        iteration = 1
        while iteration < 8:
            number.append(str(random.randint(0, 9)))
            iteration += 1
        number = "".join(number)
        return number

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance < amount:
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


huey = BankAccount("Hubert Duck")
dewey = BankAccount("Dewford Dingus Duck")
louie = BankAccount("Llewellyn Duck")

huey.deposit(400000)
huey.print_statement()
huey.add_interest()
huey.print_statement()
huey.withdraw(150)
huey.print_statement()

print("===========\n")

dewey.deposit(400)
dewey.print_statement()
dewey.add_interest()
dewey.print_statement()
dewey.withdraw(350)
dewey.print_statement()
dewey.withdraw(150)
dewey.print_statement()

print("===========\n")

louie.deposit(1000)
louie.print_statement()
louie.add_interest()
louie.get_balance()
louie.withdraw(50.83)
louie.print_statement()
