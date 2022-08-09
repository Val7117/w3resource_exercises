#!/usr/bin/env python3

# Write a Python program to find whether a given number (accept from the user) 
# is even or odd, print out an appropriate message to the user.


# Function for checking the valid input
def checkNum(num):
    try:
        int(num)
    except:
        print("Sorry, your number is wrong. Please enter one valid number.")
        exit(1)

while True:  
    givenNum = input("Please, enter your number: ")
    checkNum(givenNum)
    if int(givenNum) % 2  == 0:
        print(f"{givenNum} is an even number.")
    else:
        print(f"{givenNum} is an odd number.")

