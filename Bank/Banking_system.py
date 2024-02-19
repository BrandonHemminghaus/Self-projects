'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''

"""
Contains all the values for the user's bank details
"""
class Account_details:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    """
    Displays all the account detail values at once
    """
    def account(self):
        print("Account name: " + self.name)
        print("Account number: " + str(self.account_number))
        print("Account balance: " + str(self.balance) + "\n")

    """
    Adds to the balance value (depositing money)
    @param amount - the amount of money the user wishes to deposit
    """
    def deposit(self,amount):
        self.balance += amount

    """
    Subtracts from the balance value (withdrawing money)    
    @param amount - the amount of money the user wishes to withdraw
    @return - return amount withdrawed or -1 if withdraw is bigger than balance
    """
    def withdraw(self,amount):
        balance = self.balance
        check = balance - amount
        if check < 0:
            return -1
        else:
            self.balance -= amount
            return amount

print("Weclome to Brandon's Banking Bridge")
active = True
banking = Account_details("Brandon Hemminghaus", 16483724,0)
while(active == True):
    print("1: Account details")
    print("2: Deposit money")
    print("3: Withdraw money")
    print("4: Exit system")
    choice = int(input("Please choose an option: "))

    if(choice == 1):
        banking.account()
    elif(choice == 2):
        d = int(input("Please input the amount to deposit: "))
        banking.deposit(d)
        print("Current balance: " + str(banking.balance))
    elif(choice == 3):
        w = int(input("Please input the amount to withdraw: "))
        w_final = banking.withdraw(w)
        if w_final == -1:
            print("Not enough money in account")
        else:
            print("You have withdrawed " + str(w) + " dollars")
    elif(choice == 4):
        active = False
    else:
        print("Not a option, pick again" + "\n")