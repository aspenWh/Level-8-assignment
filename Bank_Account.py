import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self):
        amount = float(input("How much would you like to deposit?\n"))

        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("How much would you like to withdraw?\n"))

        if amount > self.balance:
            print("You do not have enough money.")
        elif amount > 0:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def display_info(self):
        print("Name:", self.name)
        print("Account #:", self.account_number)
        print(f"Balance: ${self.balance:.2f}")