# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:49:03 2020

@author: Sam
"""
import math


# Only need to check [20,19,18,17,16,15,14,13,12,11]
            
def lcm(*nums):
    numList = list(nums)
    numList.sort()
    
    if len(numList) < 2:
        return numList[0]
    elif len(numList) == 2:
        m = numList[0]
        n = numList[1]
        for x in range(m, (n * m) + 1, m):
            if x % n == 0:
                return x
    else:
        min = 1
        for x in numList:
            min = lcm(min,x)
        return min

print(lcm(20,19,18,17,16,15,14,13,12,11))

