# https://github.com/wirbelj/lab11-PK-JW.git
# Partner 1: Payton Keller
# Partner 2: Josalyn Wirbel
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def log(a, b):
    # conditions for valid log:
    # a > 0
    # b > 0 and b != 1
    if a <= 0:
        raise ValueError("Log argument must be > 0")
    if b <= 0 or b == 1:
        raise ValueError("Invalid logarithm base")
    return math.log(a, b)

def exp(a, b):
    return a ** b

