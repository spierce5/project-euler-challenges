# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:18:18 2021

@author: Sam
"""

import numpy as np

dim = 1001
matrix = np.zeros((dim,dim))
row = int(np.floor(dim/2))
col = int(np.floor(dim/2))
matrix[row][col] = 1
n = 1
num = 1
while num < dim**2 - dim + 1:
    for i in range(n):
        num += 1
        if n % 2 == 0:        
            col -= 1
            matrix[row][col] = num
        else:
            col += 1
            matrix[row][col] = num
    for j in range(n):
        num += 1
        if n % 2 == 0:
            row -= 1
            matrix[row][col] = num
        else:
            row += 1
            matrix[row][col] = num
    n += 1
for i in range(int(np.sqrt(matrix.size))-1):
    num += 1
    matrix[0][i+1] = num
            
total = -1
for i in range(int(np.sqrt(matrix.size))):
    total += matrix[i][i]
for j in range(int(np.sqrt(matrix.size))):
    total += matrix[int(np.sqrt(matrix.size))-1-j][j]

print(total)







