#!/usr/bin/env python3

# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

# Take input data
Nums = input('Please enter three numbers separated by a comma: ')

# Set how many numbers to expect. Default is 3.
maxNum = 3

# Split the numbers, using ',' as a separator 
splitNums = Nums.split(',')

# Function tests that  all entered signs to be correct values
def testingFun(data):
    for num in data:
        try:
            int(num)
        except:
            print(f'Sorry, "{num}" is not a number!')
            exit(1)

# Fucntion that sums up all numbers
def sumOfNums(numbs):
    if len(numbs) == maxNum:                        # Check that exactly {maxNum} numbers are given
        testingFun(numbs)                           # Testing function
        cleanNumbers = [int(x) for x in splitNums]  # Create a list of all three numbers
        testingNum = cleanNumbers[0]                # Additional variable for testing values
    
    # Checking for all entered number equality. 
    # If all numbers are equal, then return thhree times of their sum.
    # Otherwise return the sum of given numbers.
        for n in cleanNumbers:
            if n  != testingNum:
                res = sum(cleanNumbers)
                return print(f'The sum of your three numbers {Nums} is {res}.')
            if n == cleanNumbers[-1]:
                res = sum(cleanNumbers) * 3
                return print(f'The three times sum of your three equal numbers {Nums} is {res}.')
    else:
        return print(f'Sorry, enter EXACTLY {maxNum} numbers, separated by a comma.')               # Return if more than {maxNum} numbers have been given

sumOfNums(splitNums)                                # Passing given numbers to our 'sumOfNums' function to compute the result

