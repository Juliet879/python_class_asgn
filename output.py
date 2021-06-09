from bank import Account

acc = Account(name = "Juliet", phone= "07525556")
print(acc.borrow(4000))
print(acc.withdraw(1000))
print(acc.repay(3000))
acc.get_statement()
# print(acc.deposit(3000))
# print(acc.deposit(7000))
# print(acc.withdraw(3000))
