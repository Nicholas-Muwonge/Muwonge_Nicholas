class BankAccount:
    def __init__(self, account_holder, account_type, interest_rate=0.0):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = 0.0
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: Shs. {self.balance}")
        else:
            print("Invalidd amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: Shs. {self.balance}")
        else:
            print("INvalid amount.")

    def apply_interest(self):
        if self.account_type == "savings":
            interest = self.balance * (self.interest_rate / 100)
            self.balance += interest
            print(f"Applied interest: {interest}. New balance: Shs. {self.balance}")

    def get_balance(self):
        return self.balance

    def set_account_holder(self, name):
        self.account_holder = name
        print(f"Account holder set to: {self.account_holder}")
    def get_account_details(self):
        return {
            "Account Holder": self.account_holder,
            "Account Type": self.account_type,
            "Balance": self.balance,
            "Interest Rate": self.interest_rate
        }
if __name__ == "__main__":
    savings_account = BankAccount("Niicholas", "savings", 5.0)
    savings_account.set_account_holder("Muwonge")
    savings_account.deposit(1000)
    savings_account.withdraw(200)
    savings_account.apply_interest()
    
    print(f"Current balance: {savings_account.get_balance()}")
    print(savings_account.get_account_details())
