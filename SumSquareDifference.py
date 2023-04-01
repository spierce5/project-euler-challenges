# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 03:25:59 2020

@author: Sam
"""

import math

squares = []
sumTo100 = 0

for i in range(1, 101):
    squares.append(math.pow(i,2))

for i in range(1, 101):
    sumTo100 += i
    
print(math.pow(sumTo100,2) - sum(squares))

