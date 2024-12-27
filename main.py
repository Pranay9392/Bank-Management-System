from register import *
from database import *
from bank import *


Status = False
print("Welcome to Pranay Banking Project")
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn\n"))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                Status = True
                break
        else:
            print("Enter values specified in range")
    except ValueError:
        print("Invalid Input Try Again with Numbers")


account_number = db_query(f"SELECT account_number from customers where username = '{user}'; ")
#print(account_number[0][0])

while True:
    try:
        facility = int(input("""--Banking Services-- \n 1. Balance Enquiry\n2. Deposit\n3. Withdraw\n4. Fund Transfer\n"""))
        if facility >= 1 and facility <= 4:
            bobj = Bank(user,account_number[0][0])
            if facility == 1:
                bobj.balance_enquiry()
            if facility == 2:
                amount = int(input("Enter amount to deposit:"))
                bobj.deposit(amount)
            if facility == 3:
                amount = int(input(f"Enter Amount to withdraw:"))
                bobj.withdraw(amount)

            if facility == 4:
                amount = int(input(f"enter amount to transfer:"))
                reciever_accountnumber = int(input(f"enter reciever account number :"))
                bobj.fundtransfer(reciever_accountnumber,amount)
        else:
            print("Enter values specified in range")
    except ValueError:
        print("Invalid Input Try Again with Numbers")

