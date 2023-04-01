# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 04:08:51 2020

@author: Sam
"""

import math

for a in range(1, 1000):
    for b in range(a+1, 1000):
        if math.pow(1000-a-b, 2) == math.pow(a,2) + math.pow(b,2):
            print("a = ", a, " b = ", b, " c = ", 1000-a-b)
