class BankAccount():
    bank_name = "National Bank"
    def __init__(self,acc_holder_name,acc_number,current_balance):
        self.acc_holder_name=acc_holder_name
        self.acc_number=acc_number
        self.current_balance=current_balance
    def deposit(self):
        amount=int(input("Enter Amount to deposit ="))
        self.current_balance=self.current_balance+amount
    def withdraw(self):
        withdraw=int(input(f"Enter Amount to withdraw = "))
        if self.current_balance >= withdraw:
            self.current_balance=self.current_balance-withdraw
        else:
            print("Insufficient Balance")
    def check_balance(self):
        print(f"Current Balance= {self.current_balance}")
    def account_info(self):
        print("Account Information")
        print(f"Bank Name = {self.bank_name}")
        print(f"Account Holder = {self.acc_holder_name}")
        print(f"Account Number = {self.acc_number}")
        print(f"Current Balance = {self.current_balance}")
abdullah=BankAccount("Abdullah Zaheer",5415445,2000)
abdullah.deposit()
abdullah.withdraw()
abdullah.check_balance()
abdullah.account_info()