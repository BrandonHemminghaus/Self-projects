'''
Created on September 03, 2023
Author: Brandon Hemminghaus
'''

def single_roman(s):
    n = 0
    num = [100,50,10,5,1]
    roman = ["C","L","X","V","I"]
    for i in range(len(roman)):
        if s == roman[i]:
            n = n + num[i]
    return n

def roman_to_number(r):
    n = 0
    i = 0
    while(i < len(r)):
        r1 = single_roman(r[i])
        if i+1 < len(r):
            r2 = single_roman(r[i+1])
            if r1 >= r2:
                n = n + r1
                i = i + 1
            else:
                n = n + (r2 - r1)
                i = i + 2
        else:
            n = n + r1
            i = i + 1   
    return n

def number_to_roman(n):
    r = ""
    num = [100,90,50,40,10,9,5,4,1]
    roman = ["C","XC","L","XL","X","IX","V","IV","I"]
    while(n > 0):
        for i in range(len(roman)):
            if n >= num[i]:
                r = r + roman[i]
                n = n - num[i]
                break
    return r

print("Welcome to the roman to number converter")
print(number_to_roman(83))
print(roman_to_number("IX"))