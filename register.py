#User Registratin Signin and SignUp
from database import *
from customer import *
from bank import Bank
import random



def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("UserName Already Exists!")
        SignUp()
    else:
        print("UserName is Available Proceed!")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number =  random.randint(10000000,999999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number ='{account_number}';")
            if temp:
                continue
            else:
                print(account_number)
                break
    cobj = Customer(username,password,name,age,city,account_number)
    cobj.createuser()
    bobj = Bank(username,account_number)
    bobj.create_transaction_table()

def SignIn():
    username = input("Enter Username:")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}'; ")
    if temp:
        while True:
            password = input(f"Welcom {username.capitalize()} enter your password :")
            temp = db_query(f"SELECT password from customers WHERE username = '{username}';")
            #print(temp)
            if temp[0][0] == password: 
                print("Sign IN Successfully!")
                return username
                break
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username!")
        SignIn()

