class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        
def main():
    atm = ATM()
    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
