'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''

class Account_details:
    """
    Contains all the values for the user's bank details
    """
    name = "Brandon Hemminghaus"
    account_number = 16483724
    balance = 0

def account():
    """
    Displays all the account detail values at once
    """
    print("Account name: " + Account_details.name)
    print("Account number: " + str(Account_details.account_number))
    print("Account balance: " + str(Account_details.balance) + "\n")

def deposit(amount):
    """
    Adds to the balance value (depositing money)

    :param int amount: the amount of money the user wishes to deposit
    """
    Account_details.balance += amount

def withdraw(amount):
    """
    Subtracts from the balance value (withdrawing money)

    :param int amount: the amount of money the user wishes to withdraw
    :return -1: if withdraw is bigger than balance
    :return int amount: returns the amount withdrawed, confirming the process went throught
    """
    balance = Account_details.balance
    check = balance - amount
    if check < 0:
        return -1
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
    choice = int(input("Please choose an option: "))

    if(choice == 1):
        account()
    elif(choice == 2):
        d = int(input("Please input the amount to deposit: "))
        deposit(d)
        print("Current balance: " + str(Account_details.balance))
    elif(choice == 3):
        w = int(input("Please input the amount to withdraw: "))
        w_final = withdraw(w)
        if w_final == -1:
            print("Not enough money in account")
        else:
            print("You have withdrawed " + str(w) + " dollars")
    elif(choice == 4):
        active = False
    else:
        print("Not a option, pick again" + "\n")