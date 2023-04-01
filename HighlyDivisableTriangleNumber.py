# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:40:56 2020

@author: Sam
"""

import math

# This was an attempt to find factors recursively, but it was pretty slow

#def isPrime(k):
#    if k <= 1:
#        return False
#    if k <= 3:
#        return True
#    if k % 2 != 0:
#        for i in range(3, math.ceil(math.sqrt(k)) + 1, 2):
#            if k % i == 0:
#                return False
#        return True
#    else:
#        for i in range(2, math.ceil(math.sqrt(k)) + 1):
#            if k % i == 0:
#                return False
#        return True

#def factorize(n, arr):    #Not getting all factors; n=36 misses 6
#    if n == 1:
#        arr.append(1)
#        return 1
#    if isPrime(n):
#        arr.append(n)
#        return n
#    k = 2
#    while n % k != 0:
#        k += 1
#    arr.append(int(k))
#    arr.append(int(n//k))
#    for i in range(int(n//k), k, -1):
#        if n % i == 0:
#            arr.append(i)
#    return factorize(n/k, arr)
#
#def getFactors(n):
#    arr = [1, n]
#    factorize(n, arr)
#    factors = list(set(arr))
#    return factors
        
def getFactors(n):
    arr = [1, n]
    if n == 1:
        arr.append(1)
    else:
        for i in range(math.ceil(math.sqrt(n)), 2, -1):
            if n % i == 0:
                arr.append(i)
                arr.append(int(n//i))
    factors = list(set(arr))
    return factors
    

numFactors = 0
i = 1
n = 0
while numFactors <= 500:
    n += i
    i += 1
    num = len(getFactors(n))
    if num > numFactors:
        numFactors = num
    

print(n)





