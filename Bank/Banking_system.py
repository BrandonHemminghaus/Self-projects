'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''
name = ""
account_number = 0
balance = 0

def account(n):
    print(name)
    print(account_number)

def deposit(amount):
    balance = balance + amount
    print(balance)

def withdraw(amount):
    w = balance - amount
    if w < 0:
        return False
    else:
        balance = balance - amount
        return w

active = True
while(active == True):
    print("Weclome to Brandon's Banking Bridge")
    print("1: Account details")
    print("2: Deposit money")
    print("3: Withdraw money")
    print("4: Exit system")
    choice = input("Please choose an option: ")

    if(choice == "1"):
        print("1" + "\n")
    elif(choice == "2" + "\n"):
        print("2")
        deposit(50)
    elif(choice == "3" + "\n"):
        print("3")
        w = withdraw(50)
        if w == False:
            print("Not enough money in account")
        else:
            print("You have withdrawed " + w + "dollars")
    elif(choice == "4" + "\n"):
        active = False
    else:
        print("Not a option, pick again" + "\n")
