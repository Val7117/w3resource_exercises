#!/usr/bin/env python3

# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

givenNum = int(input("Please enter your number: "))

if givenNum < 17:
    res = abs(17 - givenNum)
    print(f"The difference between your number {givenNum} and 17 is {res}")
else:
    res = (17 - givenNum) ** 2
    print(f"Your number {givenNum} is not less than 17, so the doubled absolute difference is {res}.")
