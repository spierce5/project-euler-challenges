# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:28:57 2021

@author: Sam
"""
from itertools import permutations

pandigital = set()

digits = [1,2,3,4,5,6,7,8,9]
perms = permutations(digits)
for p in perms:
    num = 0
    for dig in p:
        num *= 10
        num += dig
    pandigital.add(int(num))
    
maxPan = 0
for num in range(2,9999):               #9999 because 9999*2 gives 5 digits + 4 digits for 9999*1; anything more and
    result = ''                         #we get too many digits
    i = 1
    while len(result) < 9:
        result += str(num * i)
        i += 1
    if len(result) == 9:
        if int(result) in pandigital:
            if int(result) > maxPan:
                maxPan = int(result)
        
print(maxPan)