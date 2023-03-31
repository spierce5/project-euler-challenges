# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:33:26 2020

@author: Sam
"""

factorials = {}

def factorial(n):
    if n == 1: 
        return 1
    elif n in factorials:
        return factorials[n]
    else:
        return n * factorial(n-1)
    
number = str(factorial(100))

sumOfDigits = 0
for digit in number:
    sumOfDigits += int(digit)

print(sumOfDigits)