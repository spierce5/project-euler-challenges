# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:13:48 2020

@author: Sam
"""
import math

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

n = 600851475143

for i in range(2, math.ceil(n//2)):
    if n % i == 0:
        temp = n//i
        if isPrime(temp):
            print(temp)
            break

