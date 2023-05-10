# filter_functions.py

import math


# Here is example of filter functions

# Odd number
def odd(a: float):
    return math.isclose(a % 2, 0)


# Greater than 5
def greater_thar_five(a: float):
    return a > 5


# Palindrome control
def palindrome(s: str):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# Contain A
def contain_a(s: str):
    s = s.replace(" ", "").lower()
    return -1 == s.find("a")
