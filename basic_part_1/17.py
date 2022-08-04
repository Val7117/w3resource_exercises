#!/usr/bin/env python3

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Please, enter your number: "))

if (abs(1000 - num) <= 100) or (abs(2000 - num) <= 100):
    print('Yes')
else:
    print('No')
