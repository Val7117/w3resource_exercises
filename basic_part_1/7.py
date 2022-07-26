#!/usr/bin/env python3

# Write a Python program to accept a filename from the user and print the extension of that.

fileName = input("Enter your filename: ")
extension = fileName.split('.')[-1]

print(f"Your extension is: {extension}") 
