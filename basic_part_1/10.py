#!/usr/bin/env python3

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
while True:

    number = input("Please enter your number: ")

    try:
        int(number)
        res = int(number) + int(number * 2) + int(number * 3)
        print(f"Your result is {res}")
    except:
        print("Sorry, incorrect input data. Please enter an integer.") 

