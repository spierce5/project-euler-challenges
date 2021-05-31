# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:43:42 2020

@author: Sam
"""
import math


def flipNumber(n):
    if n < 10000 or n > 998001:
        return None
    elif n < 100000: 
        ones = math.floor(n / 10000)
        y = n - (ones * 10000)
        tens = math.floor(y / 1000)
        z = y - (tens * 1000)
        hunds = math.floor(z / 100)
        k = z - (hunds * 100)
        thous = math.floor(k / 10)
        tenthous = k - (thous * 10)
        
        return (10000 * tenthous) + (1000 * thous) + (100 * hunds) + (10 * tens) + ones
    else:
        ones = math.floor(n / 100000)
        y = n - (ones * 100000)
        tens = math.floor(y / 10000)
        z = y - (tens * 10000)
        hunds = math.floor(z / 1000)
        k = z - (hunds * 1000)
        thous = math.floor(k / 100)
        l = k - (thous * 100)
        tenthous = math.floor(l / 10)
        hunthous = l - (tenthous * 10)
        
        return (100000 * hunthous) + (10000 * tenthous) + (1000 * thous) + (100 * hunds) + (10 * tens) + ones
   
target = 0 

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if (i * j) == flipNumber(i * j) and (i * j) > target:
            target = i * j
            print(i, j)
    
print(target)
