# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:41:35 2021

@author: Sam
"""

def getDigits(n):
    arr = list(str(n))
    return arr

powers = set()

for i in range(2,1000000):
    total = 0
    dig = getDigits(i)
    while total <= i and dig:
        total += int(dig.pop())**5
        
    if total == i:
        powers.add(i)
        
print(sum(powers))