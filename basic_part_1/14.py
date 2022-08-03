#!/usr/bin/env python3

# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import datetime

print("Please, enter your date in a numeric format, using a comma as a separator.(E.g. 2000, 12, 31)")

# Two input prompts

firstDate = input("Enter your first date: ")
secondDate = input("Enter your second date: ")

# Split two input strings
firstDateSplit = firstDate.split(',')
secondDateSplit = secondDate.split(',')

# Create two lists for each date, transforming strings in lists to integers in lists.
date1 = [int(i) for i in firstDateSplit]
date2 = [int(j) for j in secondDateSplit]


# Calculate the difference
delta = datetime.date(date1[0], date1[1], date1[2]) - datetime.date(date2[0], date2[1], date2[2])

# Extract only the number of days
days = abs(delta.days)

# Print the result
print(f"The number of days between dates ({firstDate}) and ({secondDate}) is {days}.")
