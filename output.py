# syntax error -Error caused by wrong syntax
# Exception - Correct syntax,wrong or impossible execution e.g TypeError ZeroDivisionError
#    If an exeption occers you should handle an exception 

from bank import MobileMoneyAccount

user = MobileMoneyAccount(name = "Juliet", phone = "7896356",service_provider="Safaricom")
user2 = MobileMoneyAccount(name = "Sindet", phone = "23554",service_provider="Safaricom")

print(user.deposit(500))
print(user.buy_airtime(50))
print(user.buy_someone_airtime(30,user2))
user.get_statement()




























# acc1 = Account(name = "Juliet", phone= "07525556")
# acc2 = Account(name = "Lynne", phone= "07525556")
# print(acc1.transfer("One thousand",acc2))
# print(acc1.transfer(1000,acc2))
# print(acc1.deposit(1000))
# print(acc1.transfer(500,acc2))
# print(acc1.balance)
# print(acc2.balance)



# print(acc.borrow(4000))
# print(acc.withdraw(1000))
# print(acc.repay(3000))
# acc.get_statement()
# print(acc.deposit(3000))
# print(acc.deposit(7000))
# print(acc.withdraw(3000))


