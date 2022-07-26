#!/usr/bin/env python3

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

seq = input("Please, enter comma-separated numbers: ")

listNum = seq.split(',')
tupleNum = tuple(seq.split(','))

print("List:", listNum)
print("Tuple:", tupleNum)

