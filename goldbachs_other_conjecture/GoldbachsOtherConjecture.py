# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:07:11 2021

@author: Sam
"""
import numpy as np
import math

primes = [2]

def isPrime(n): 
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else: 
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
        return True
    
def getNextPrime(n):
    if not isPrime(n):
        return None
    elif n == 2:
        return 3
    else:
        notPrime = True
        i = n + 2
        while notPrime:
            if isPrime(i):
                notPrime = False
                primes.append(int(i))
                return i
            else:
                i += 2


linComb = np.zeros((1000,1000))
for i in range(1,1000):
    linComb[i][0] = int(2 * (i**2))
    if i == 1:
        linComb[0][i] = 2
    else:
        linComb[0][i] = int(getNextPrime(linComb[0][i-1]))
        
for row in range(1, int(math.sqrt(linComb.size))):
    for column in range(1, int(math.sqrt(linComb.size))):
        linComb[row][column] = int(linComb[row][0] + linComb[0][column])


i = 9
counterExample = False
while not counterExample:
    if not isPrime(i):
        if i not in linComb:
            print(i)
            counterExample = True
    i += 2
    
    
# Next time use this for primes
# Sieve of Eratosthenes
#primes = set(range(2, 10000))  
#p = 2
#while p < 100:
#    if p in primes:
#        for q in range(2, 10000 // p + 1):
#            primes.discard(p * q)
#    p += 1
        

        
        
        
        