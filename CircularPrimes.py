# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:30:25 2020

@author: Sam
"""
import math
from itertools import permutations

def getDigits(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    return digits

def isPrime(k):
    if k <= 1:
        return False
    elif k <= 3:
        return True
    elif k % 2 != 0:
        for i in range(3, math.ceil(math.sqrt(k)) + 1, 2):
            if k % i == 0:
                return False
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True
# Method to get all variants of permutation defined by order of digits in number
def getPerms(n):
    digits = getDigits(n)
    result = []
    for i in range(len(digits)):
        num = str(digits[i])
        for j in range(i+1, len(digits) + i):
            if j < len(digits):
                num += str(digits[j])
            else:
                num += str(digits[j - len(digits)])
        if len(str(int(num))) == len(str(n)):
            result.append(int(num))
    return result

# Not sure why this isn't working. Not finding any numbers with more than four digits
#This is checking all combinations of digits, but need only check variants of one permutation eg. (123)=(231)=(312)
count = 1                       #Start at 1 to include 2
lst = []
for i in range(3, 1000000, 2):
    circPrime = False
    if i not in lst:
        if isPrime(i):
            circPrime = True
            perm = set(getPerms(i))
            for num in perm:
                if not isPrime(num):
                    circPrime = False
    if circPrime:
        count += len(perm)
        lst.extend(perm)
        
print(count)
    

        


        
        
        
        
        
        