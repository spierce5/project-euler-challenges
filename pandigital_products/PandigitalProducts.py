# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:26:40 2021

@author: Sam
"""
from itertools import permutations

pandigital = {}                 # Key: product, Value: lists of products

digits = [1,2,3,4,5,6,7,8,9]

perms = permutations(digits)

for p in perms:
    a = (p[0] * 10) + p[1]
    b = (p[2] * 100) + (p[3] * 10) + p[4]
    c = (p[5] * 1000) + (p[6] * 100) + (p[7] * 10) + p[8]
    if a * b == c:
        try:
            pandigital[c].append([a,b])
        except KeyError:
            pandigital[c] = [[a,b]]
    a = (p[0] * 1000) + (p[1] * 100) + (p[2] * 10) + p[3]
    b = p[4]
    c = (p[5] * 1000) + (p[6] * 100) + (p[7] * 10) + p[8]
    if a * b == c:
        try:
            pandigital[c].append([a,b])
        except KeyError:
            pandigital[c] = [[a,b]]
            
print(sum(pandigital))