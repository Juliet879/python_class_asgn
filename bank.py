# class account,3 attributes,3methods

class Account:
    def __init__(self,acc_name,acc_number,balance):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.balance = balance

    def withdraw(self,withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        balance = self.balance - self.withdrawal_amount
        return f"{self.acc_name} your balance after withdrawal is {balance}"

    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        return f"Hello, {self.acc_name} you have deposited {self.deposit_amount}"

    def check_balance(self):
        return f"{self.acc_name},account number {self.acc_number} your current balance is {self.balance}"


