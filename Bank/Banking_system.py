'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''

class Account_details:
    name = "Brandon Hemminghaus"
    account_number = 16483724
    balance = 0

def account():
    print("Account name: " + Account_details.name)
    print("Account number: " + str(Account_details.account_number))
    print("Account balance: " + str(Account_details.balance) + "\n")

def deposit(amount):
    Account_details.balance += amount

def withdraw(amount):
    balance = Account_details.balance
    w = balance - amount
    if w < 0:
        return False
    else:
        Account_details.balance -= amount
        return amount

print("Weclome to Brandon's Banking Bridge")
active = True
while(active == True):
    print("1: Account details")
    print("2: Deposit money")
    print("3: Withdraw money")
    print("4: Exit system")
    choice = input("Please choose an option: ")
    choice_int = int(choice)

    if(choice_int == 1):
        account()
    elif(choice_int == 2):
        d = input("Please input the amount to deposit: ")
        d_int = int(d)
        deposit(d_int)
        print("Current balance: " + str(Account_details.balance))
    elif(choice_int == 3):
        w = input("Please input the amount to withdraw: ")
        w_int = int(w)
        w_final = withdraw(w_int)
        if w_final == False:
            print("Not enough money in account")
        else:
            print("You have withdrawed " + str(w) + " dollars")
    elif(choice_int == 4):
        active = False
    else:
        print("Not a option, pick again" + "\n")