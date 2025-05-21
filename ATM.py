class ATM:
    balance = 0

    def deposit(amount):
        if amount > 0:
            balance += amount
            print(f"Deposited: Shs. {amount}")
            print(f"New balance: Shs. {balance}")
        else:
            print("No depposit made.")

    def withdraw(amount):
        if amount <=0:
            print("Enter a valid withdrawal amount.")
        elif amount <= balance:
            balance -= amount
            print(f"Withdrawn: Shs. {amount}")
            print(f"New balance: Shs. {balance}")
        else:
            print("Insufficient balance.")

    def check_balance(balance):
        print(f"Current balance: Shs. {balance}")
        
def main():
    atm = ATM()
    while True:
        print("\nWelcome to Nicho's ATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Thank you for using Nicho's ATM.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()