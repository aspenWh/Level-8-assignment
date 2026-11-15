from Bank_Account import BankAccount

# Function for option 1
def make_deposit(account):
    account.deposit()


# Function for option 2
def make_withdrawal(account):
    account.withdraw()


# Function for option 3
def view_account(account):
    account.display_info()


# Main program
print("Welcome to the Bank of Spencer!")

name = input("Please enter your name:\n")

account = BankAccount(name)

while True:
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input()

    if choice == "1":
        make_deposit(account)

    elif choice == "2":
        make_withdrawal(account)

    elif choice == "3":
        view_account(account)

    elif choice == "4":
        print("Thank you for your business!")
        break

    else:
        print("Invalid choice. Please try again.")