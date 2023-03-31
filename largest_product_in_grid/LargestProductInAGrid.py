# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 04:48:55 2020

@author: Sam
"""

matrix = []
with open('C:/Users/Sam/Desktop/Current_Scripts/Python_Scripts/ProjectEuler/TextFiles/grid.txt', 'r') as fp:
    Lines = fp.readlines()
    for line in Lines:
        arr = line.strip('\n').split(' ')
        intArr = [int(x) for x in arr]
        matrix.append(intArr)

# iterate through matrix and save largest product
largestProduct = 1

#Horizontal
for i in range(20):
    for j in range(17):
        if matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3] > largestProduct:
            largestProduct = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
            
#Vertical            
for j in range(20):
    for i in range(17):
        if matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j] > largestProduct:
            largestProduct = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
            
#Forward Diagonal
for i in range(17):
    for j in range(17):
        if matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3] > largestProduct:
            largestProduct = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
            
#BackwardDiagonal
for i in range(17):
    for j in range(19, 2, -1):
        if matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3] > largestProduct:
            largestProduct = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]

print(largestProduct)




