#!/usr/bin/env python3

# Write a Python program to get the Python version you are using.

import sys

version = sys.version_info

maj = version.major
mino = version.minor
mic = version.micro

print(f"Your Python's version is {maj}.{mino}.{mic}")
