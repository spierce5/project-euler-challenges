# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:40:31 2021

@author: Sam
"""

import re
import fractions as fr

seqLen = {}
for q in range(2, 1000):
    if q % 2 != 0 and q % 5 != 0:
        div = False
        i = 0
        while not div:
            i += 1
            if (10**i - 1) % q == 0:
                div = True
        seqLen[i] = fr.Fraction(1,q)
        
print(seqLen[max(seqLen)])
print(max(seqLen))



















