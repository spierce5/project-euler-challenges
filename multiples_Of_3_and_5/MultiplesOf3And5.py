# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:23:34 2020

@author: Sam
"""

multiples3 = [] 
multiples5 = []
multiples15 = []
sumTotal = 0

for i in range (1, 334):
    if (3 * i < 1000):
        multiples3.append(3 * i)
    if (5 * i < 1000):
        multiples5.append(5 * i)
    if (15 * i < 1000):
        multiples15.append(15 * i)
        
sumTotal = sum(multiples3) + sum(multiples5) - sum(multiples15)
        
print(sumTotal)
print(multiples3)
print(multiples5)
print(multiples15)