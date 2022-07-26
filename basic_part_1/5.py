#!/usr/bin/env python3

# Program which accepts the user's first and last name and print them 
# in reverse order with a space between them.

firstName = input("Enter your first name: ").lower()[::-1]
lastName = input("Enter your last name: ").lower()[::-1]

newFirstName = firstName[0].upper() + firstName[1:] 
newLastName = lastName[0].upper() + lastName[1:]

print(f"Your first and laste names in reverse order are: {newFirstName} {newLastName}")

