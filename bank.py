#BANK SERVICES
from database import *
import datetime
class Bank:
    def __init__(self,username,account_number):
        self.__username = username
        self.__account_number = account_number
        
    def create_transaction_table(self):
        db_query(f"""CREATE TABLE IF NOT EXISTS {self.__username}_transactions
                 (timedate VARCHAR(30),
                 account_number INTEGER,
                 remarks VARCHAR(30),
                 amount INTEGER);
                 """)
    def balance_enquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(f"{self.__username} balance is {temp[0][0]}\n")
    
    def deposit(self,amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        new_bal = temp[0][0] + amount
        db_query(f"UPDATE customers SET balance = {new_bal} WHERE username = '{self.__username}';")
        mydb.commit()
        db_query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.datetime.now()}',{self.__account_number},'deposit',{amount});")
        print(f"{self.__username} Amount {amount} is Sucessfully Deposited in Your Account {self.__account_number}\n")
        self.balance_enquiry()

    
    def withdraw(self,amount):
        account_balance = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount>account_balance[0][0]:
            print(f"Insufficient Balance!")
        else:
            new_bal = account_balance[0][0] - amount
            db_query(f"UPDATE customers SET balance = {new_bal} WHERE username = '{self.__username}';")
            mydb.commit()
            db_query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.datetime.now()}',{self.__account_number},'withdraw',{amount})")
            print(f"{self.__username} Amount {amount} is Sucessfully Withdrawn from Your Account {self.__account_number}\n")
            self.balance_enquiry()

    def fundtransfer(self,reciever_accountnumber,amount):
        account_balance = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount>account_balance[0][0]:
            return f"Insufficient Balance!"
        else:
            reciever_balance = db_query(f"SELECT balance FROM customers WHERE account_number = {reciever_accountnumber};")
            if not reciever_balance:
                print(f"Account number not found!")
            else:
                new_abal = account_balance[0][0] - amount
                db_query(f"UPDATE customers SET balance = {new_abal} WHERE username = '{self.__username}';")
                db_query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.datetime.now()}',{self.__account_number},'fund transfer -> {reciever_accountnumber}',{amount});")

                new_rbal = reciever_balance[0][0] + amount
                reciever_username = db_query(f"SELECT username FROM customers where account_number = '{reciever_accountnumber}';")
                db_query(f"UPDATE customers SET balance = {new_rbal} WHERE account_number = {reciever_accountnumber};")
                db_query(f"INSERT INTO {reciever_username[0][0]}_transactions VALUES ('{datetime.datetime.now()}',{self.__account_number},'fund transfer from {self.__account_number}',{amount});")
                mydb.commit()
                print(f"{amount} transfered to {reciever_accountnumber}\n")
                self.balance_enquiry()