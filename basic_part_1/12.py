#!/usr/bin/env python3

# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

enteredData = input("Please enter a month and a year in a numeric format using , as a delimiter: ")

splitData = enteredData.split(',')

month = int(splitData[0])
year = int(splitData[1])

outputData = calendar.month(year, month)
print(outputData)

