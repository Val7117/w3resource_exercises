#!/usr/bin/env python3

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

# Import inspect module

import inspect

while True:
    input_data = input("Please enter the name of build-in Python function(s), using , as a delimeter: ")
    functions = input_data.split(',')

    for function in functions:
        try:
            res = inspect.getdoc(eval(function))
            print(f"\nResult for function {function}\n{res}\n")
            print("*********************************************************")
        except:
            print(f"Sorry, cannot find the function {function}\n")
