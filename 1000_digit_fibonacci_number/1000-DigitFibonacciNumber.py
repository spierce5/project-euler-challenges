# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:50:23 2021

@author: Sam
"""

fib_Terms = dict()

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 1
    elif n in fib_Terms:
        return fib_Terms[n]
    else: 
        fib_Terms[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)
    
def getNumDigits(n):
    return len(str(n))

found = False
i = 1
while not found:
    if len(str(fibonacci(i))) == 1000:
        found = True
    else:
        i += 1
        
print(i)
