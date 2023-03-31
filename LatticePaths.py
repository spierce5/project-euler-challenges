# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:37:07 2020

@author: Sam
"""
import math
import numpy as np

n = 20

lattice = np.zeros((n+1,n+1))

for row in lattice:
    row[n] = 1
for j in range(n):
    lattice[n][j] = 1
for j in range(n-1, -1, -1):
    for i in range(n-1, -1, -1):
        lattice[i][j] = lattice[i][j+1] + lattice[i+1][j]
        
    
print(lattice[0][0])

sol = math.factorial(2*n) / math.pow(math.factorial(n),2)
print(sol)