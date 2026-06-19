class BankAccount:
    def __init__(self, account_number, account_holder, initialAmount=0):
        self.number = account_number
        self.name = account_holder
        self.balance = initialAmount
        print(f"Account created for {self.name} \nAccount number {self.number} \nBalance = ${self.balance:.2f}")
    def get_balance(self):
        print(f"Balance of {self.name}: ${self.balance:.2f}")
    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit successful")
        self.get_balance()