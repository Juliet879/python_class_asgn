# class account,3 attributes,3methods

class Account:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.balance = 0
        self.transaction_fee = 30
        self.loan = 0
        self.loan_limit = 5000
        self.loan_interest = 5 

    def deposit(self,amount):
        if amount<=0:
            return f"please deposit a valid amount"

        else:
            self.balance += amount
            return f"Hello, {self.name} you have deposited {amount} ,new balance is {self.balance}"

     
    def withdraw(self,withdrawal_amount):
        total = withdrawal_amount + self.transaction_fee
        if withdrawal_amount <= 0:
            return "please enter valid amount"

        elif total > self.balance:
            return "Insufficient balance"  

        else:

            self.balance -= total
            return f"Hello {self.name} you have successfully withdrawn {withdrawal_amount} account balance is {self.balance}"

    def borrow(self,loan):
        loan_fees = self.loan_interest * loan / 100
        
        if loan < 0:
            return "Please enter a valid amount"

        elif loan > self.loan_limit:
            return "The amount exeedes the loan limit,please enter a lower amount"

        elif  self.loan > 0:
            return "You have an outstanding loan"

        else:
            repay = loan + loan_fees
            self.loan += repay
            self.balance += loan
            return f"You have received a loan of {loan} your account balance now is {self.balance},the amount you will repay is {self.loan}"




