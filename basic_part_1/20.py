#!/usr/bin/env python3

# Write a Python program to get a string which is n (non-negative integer) 
# copies of a given string.

while True:
    givenString = input("Please, enter your string: ")
    if givenString == 'stop':
        break
    givenNum = input("Please, enter your n (non-negative integer): ")

    # Print the givenTimes multiplied by the givenNum
    print(givenString * int(givenNum))
