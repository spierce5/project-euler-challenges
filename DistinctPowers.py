# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:36:45 2021

@author: Sam
"""

powers = set()

for a in range(2,101):
    for b in range(2,101):
        powers.add(a**b)
        
print(len(powers))