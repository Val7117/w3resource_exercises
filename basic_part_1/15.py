#!/usr/bin/env python3

# Write a Python program to get the volume of a sphere with a given radius.

import math

radius = input("Please enter a radius of your sphere: ")

try:
    int(radius)
except:
    print("Sorry, wrong value of the radius. Please, try again and enter the correct radius.") 
    exit(1)

volume = 4 / 3 * math.pi * int(radius) ** 3

print(f"The volume of your sphere is {volume}.")
