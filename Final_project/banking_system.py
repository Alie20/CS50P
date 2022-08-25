import sys
import csv
from csv import writer
import pandas as pd

class Account():
    next_account_no = 0
    def __init__(self,first_name,last_name,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        Account.next_account_no +=  1 

    @property
    def first_name(self):
        return self._frist_name
    
    @first_name.setter
    def first_name(self,first_name):
        if not first_name:
            raise ValueError
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,last_name):
        if not last_name:
            raise ValueError
        self._last_name = last_name

    @property
    def balance(self):
        return self._balance
    
    @last_name.setter
    def balance(self,balance):
        if balance < 0:
            raise ValueError
        self._balance = balance
    
    def __str__(self):
        return f"first_name: {self._first_name} \nlast_name: {self._last_name} \nbalance: {self._balance}\nAccount_no: {Account.next_account_no}"

    def get_last_account_no(self):
        return Account.Acount_no
    

class Bank(Account):
    def __init__(self,first_name,last_name,balance):
        super().__init__(first_name,last_name,balance)

    @classmethod
    def create_account(cls):
        first_name = input("Please Enter your first Name")
        last_name = input("Please Enter your second Name")
        balance = int(input("Please Enter your balance"))
        a = [{'Account_No':Account.next_account_no,
             'first_name':first_name,
             'last_name':last_name,
             'balance':balance
             }]
        header = ['Account_No', 'first_name', 'last_name', 'balance']
        with open('data.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writerows(a)

        print("######Congratulation You have Created New Account ############")
        return cls(first_name,last_name,balance);

    def deposit(self,amount):
        self.balance += amount 

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient Fund"
        self.balance -= amount



def main():
    #Reading data
    file = open('data.csv')
    csvreader = csv.DictReader(file)
    a ={}
    for row in csvreader:
        last_account_no = row['Account_No']

    df = pd.read_csv("data.csv")
    print(df)

        
    while (True):
        print("**********BANKING SYSTEM ***************\n")
        print("Please Enter Number from 1 to 7 to select from the following\n")
        print("\t 1. Create new Account\n")
        print("\t 2. Balance Enquiry\n")
        print("\t 3. Deposit\n")
        print("\t 4. Withdrawal\n")
        print("\t 5. Show all Accounts\n")
        print("\t 6. Quit\n")
        choice = int(input("Please Enter number 1 to 7:  "))
        if (choice == 1):
            print(Bank.create_account())

        elif (choice == 2):
            account= input("Please Enter your Account_no")
            try:
                print(f"Your account balance is {a[account]['balance']}")
            except ValueError:
                raise("Account No is not correct")
        elif (choice == 3):
            account= input("Please Enter your Account_no")
            amount = int(input("please Enter amount"))
            try:
                a[account]['balance'] = int(a[account]['balance']) + amount
                df.loc[account, 'balance'] = a[account]['balance']

                print(f"Your account balance is {a[account]['balance']}")
            except ValueError:
                raise("Account No is not correct")
        elif (choice == 4):
            account= input("Please Enter your Account_no")
            amount = int(input("please Enter amount"))
            try:
                if int(a[account]['balance'])< amount:
                    return "Insufficient Fund"
                a[account]['balance'] = int(a[account]['balance']) - amount
                df.loc[account, 'balance'] = a[account]['balance']
                print(f"Your account balance is {a[account]['balance']}")
            except ValueError:
                raise("Account No is not correct")
        elif (choice == 5 ):
            for _ in a:
                print(f"Account_no: {a[_]['Account_No']}\nFirst_name: {a[_]['first_name']}\nLast_name: {a[_]['last_name']}\nBalance: {a[_]['balance']}\n")

        elif (choice == 6):
            sys.exit()
       
if __name__ == "__main__":
    main()         
    
