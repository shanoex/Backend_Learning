from bank import *

account1= BankAccount("1000","John", 1000)
sarah= BankAccount("1001","Sarah", 2000)
sarah.get_balance()

account1.transfer(5000, sarah)

Tanmay= InterestRewardAccount("1002", "Tanmay", 500)
Tanmay.deposit(1000)
Tanmay.transfer(200, sarah)

blaziken = SavingsAccount(1003, "Blaziken", 1000)
