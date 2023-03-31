# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:10:18 2021

@author: Sam
"""

from itertools import permutations

digits = ['0','1','2','3','4','5','6','7','8','9']
perms = list(permutations(digits))

result = ''
for digit in perms[999999]:
    result += digit
    
print(result)
