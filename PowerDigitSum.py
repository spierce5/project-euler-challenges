# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:39:23 2020

@author: Sam
"""
import math

digSum = 0
for n in str(2**1000):
    digSum += int(n)

print(digSum)
