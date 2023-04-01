# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:05:42 2020

@author: Sam
"""


fib_Terms = dict()

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    elif n in fib_Terms:
        return fib_Terms[n]
    else: 
        fib_Terms[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

k=1
evenSum = 0
while fibonacci(k) <= 4000000:
    if fibonacci(k) % 2 == 0:
        evenSum += fibonacci(k)
    k += 1
    
print(evenSum)
        
