# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 04:31:07 2020

@author: Sam
"""

import math

def isPrime(k):
    if k <= 1:
        return False
    if k <= 3:
        return True
    if k % 2 != 0:
        for i in range(3, math.ceil(math.sqrt(k)) + 1, 2):
            if k % i == 0:
                return False
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True
    
sumOfPrimes = 0
for i in range(1, 2000000):
    if isPrime(i):
        primes.append(i)
        sumOfPrimes += i
        
print(sumOfPrimes)
