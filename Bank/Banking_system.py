'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''

"""
Contains all the values for the user's bank details
"""
class Account_details:
    name = "Brandon Hemminghaus"
    account_number = 16483724
    balance = 0

"""
Displays all the account detail values at once
"""
def account():
    print("Account name: " + Account_details.name)
    print("Account number: " + str(Account_details.account_number))
    print("Account balance: " + str(Account_details.balance) + "\n")

"""
Adds to the balance value (depositing money)
@param amount - the amount of money the user wishes to deposit
"""
def deposit(amount):
    Account_details.balance += amount

"""
Subtracts from the balance value (withdrawing money)    
@param amount - the amount of money the user wishes to withdraw
@return - return amount withdrawed or -1 if withdraw is bigger than balance
"""
def withdraw(amount):
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