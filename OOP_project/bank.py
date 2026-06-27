class BalanceError(Exception):
    pass


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
    def viable_Transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceError("Insufficient funds")
    def withdraw(self, amount):
        try:
            self.viable_Transaction(amount)
            self.balance -=amount
            print("\nWithdrawal successful")
            self.get_balance()
        except BalanceError as e:
            print(f"\nWithdrawal failed: {e}")
    def transfer(self, amount, recipient):
        try:
            self.viable_Transaction(amount)
            self.withdraw(amount)
            recipient.deposit(amount)
            print(f"\nTransfer successful to {recipient.name}")
        except BalanceError as e:
            print(f"\nTransfer failed: {e}")    

class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposit successful with interest reward")
        self.get_balance()
class SavingsAccount(InterestRewardAccount):
    def __init__(self, initialAmount, account_holder):
        super().__init__(initialAmount, account_holder)
        self.fee = 5
    def withdraw(self,amount):
        try:
            self.viable_Transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\n Withdrawal successful")
            self.get_balance()
        except BalanceError as e:
            print(f"\nWithdrawal failed: {e}")