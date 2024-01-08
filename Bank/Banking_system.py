'''
Created on January 06, 2024
Author: Brandon Hemminghaus
'''

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
    elif(choice == "3" + "\n"):
        print("3")
    elif(choice == "4" + "\n"):
        active = False
    else:
        print("Not a option, pick again" + "\n")
