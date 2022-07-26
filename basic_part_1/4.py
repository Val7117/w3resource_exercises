#!/usr/bin/env python3

# Calculate area with the given radius

import math

radius = input("Please, enter your radius:\nr = ")

try:
    float(radius)
except:
    print("Sorry, you've entered the wrong radius. Please restart the program" \
    "and start again.")
    exit(1)

res = math.pi * float(radius) ** 2
print(f"Area = {res}")
