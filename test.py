from datetime import datetime
today = datetime.today()
print(today)

class Bank_Account:
    def __init__(self, account_number, balance, owner_name, date_opened = today):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        
    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"Ksh{amount} deposited successfully to account:{self.account_number}\n New balance is {self.balance}")
        else:
            print("please try depositing again")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Ksh{amount} withdrawn successfully")
        else:
            print("Insufficient balance")
    
    def display_info(self):
        print(f"account_number : {self.account_number}")
        print(f"balance : {self.balance}")
        print(f"owner_name : {self.owner_name}")
        print(f"date_opened : {self.date_opened}")
        
account1 = Bank_Account(1234567890,50000,"Mary Mwangi","24-04-2025")
print(account1)
account1.deposit(5000)
account1.withdraw(2000)
account1.display_info()

account2 = Bank_Account(9876543210,30000,"Mark Munyao","05-01-2025")
print(account2)
account2.deposit(7000)
account2.withdraw(3000)
account2.display_info()