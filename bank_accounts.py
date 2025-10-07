class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Complete")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("Withdrawal Complete")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdrawal Interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\nBeginning Transfer....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer complete!\n**********")
        except BalanceException as error:
            print(f"Transfer Interrupted: {error}")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("Deposit Complete (with 5% interest bonus).")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f"Withdrawal completed (with ${self.fee} fee).")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdrawal Interrupted: {error}")

# ---------- USER INTERACTIVE MENU ----------
def main():
    print("Welcome to the Python Bank System 💰")

    accounts = {}

    while True:
        print("\nChoose an option:")
        print("1. Create a Bank Account")
        print("2. Create a Savings Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Check Balance")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter account name: ")
            amount = float(input("Enter initial deposit: "))
            accounts[name] = BankAccount(amount, name)

        elif choice == '2':
            name = input("Enter account name: ")
            amount = float(input("Enter initial deposit: "))
            accounts[name] = SavingsAcct(amount, name)

        elif choice == '3':
            name = input("Enter account name: ")
            if name in accounts:
                amt = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amt)
            else:
                print("Account not found!")

        elif choice == '4':
            name = input("Enter account name: ")
            if name in accounts:
                amt = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amt)
            else:
                print("Account not found!")

        elif choice == '5':
            from_acc = input("Transfer from (account name): ")
            to_acc = input("Transfer to (account name): ")
            if from_acc in accounts and to_acc in accounts:
                amt = float(input("Enter amount to transfer: "))
                accounts[from_acc].transfer(amt, accounts[to_acc])
            else:
                print("One or both accounts not found!")

        elif choice == '6':
            name = input("Enter account name: ")
            if name in accounts:
                accounts[name].getBalance()
            else:
                print("Account not found!")

        elif choice == '7':
            print("Thank you for banking with us. Goodbye! 👋")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
