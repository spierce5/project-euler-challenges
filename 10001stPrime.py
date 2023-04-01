# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 03:35:49 2020

@author: Sam
"""

import math

# If k is odd, only check odd numbers
tic = time.perf_counter()
def isPrime(k):
    if k % 2 != 0:
        for i in range(3, math.ceil(math.sqrt(k)) + 1, 2):
            if k % i == 0:
                return False
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(k))):
            if k % i == 0:
                return False
        return True
    

primes = {1 : 2, 2 : 3}

i = 5
n = 3
while len(primes) < 10001:
    if isPrime(i):
        primes[n] = i
        n += 1
    i += 2
    
print(primes[10001])
