# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 02:51:01 2021

@author: Sam
"""

from itertools import product
import math

#Sieve of Eratosthenes
n = 2000000
primes = set(range(2, n))  
p = 2
while p < math.sqrt(n):
    if p in primes:
        for q in range(2, n // p + 1):
            primes.discard(p * q)
    p += 1
    
def changeDigits(arr, idx, n):
    newArr = arr.copy()
    for i in idx:
        if i < len(arr):
            newArr[i] = n
    return newArr


found = False
for p in primes:   
    if not found:
        digits = list(str(p))
        matches = []
        for case in product((0,1), repeat=len(digits)):
            if not found:
                idx = []
                matches.clear()
                for i in range(len(case)):
                    if case[i] == 1:
                        idx.append(i)
                for j in range(10):
                    newArr = changeDigits(digits, idx, str(j))
                    num = "".join(newArr)
                    if int(num) in primes and len(str(int(num))) == len(str(p)):
                        matches.append(int(num))
                if len(matches) == 8:
                    found = True
            else:
                print(matches)
                break
    
# The main trick was to use itertools product to create all the combinations of 0 and 1
# for the given number of repeats. This in a way resembles nested for loops, but one does not need to
# specify how many nested loops to use. Taking the results from the products we add the to a list of indices
# which we then give to the changeDigits method to replace those indices in the number with the given number. 

    
    