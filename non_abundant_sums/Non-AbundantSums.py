# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:46:35 2021

@author: Sam
"""
import math 

def getDivisors(n): 
    div = set()
    div.add(1)
    if n > 3:
        for i in range(int(math.sqrt(n) + 1), 1, -1):
            if i not in div:
                if n % i == 0:
                    div.add(i)
                    div.add(n//i)
    return div
abundant = []   
nonASums = set()

for i in range(1, 28124):
    nonASums.add(i)

for i in range(1, 28124):
    if sum(getDivisors(i)) > i:
        abundant.append(i)
        
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] < 28124:
            nonASums.discard(abundant[i] + abundant[j])
    
print(sum(nonASums))
    
