# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:13:00 2020

@author: Sam
"""
import numpy as np
import math

# Creating matrix from text file
arr = []
with open(r'C:\Users\Sam\Desktop\Current_Scripts\Python_Scripts\ProjectEuler\TextFiles\triangle.txt', 'r') as fp:
    Lines = fp.readlines()
    matrix = np.zeros((len(Lines),len(Lines)))
    for i in range(len(Lines)):
        Lines[i] = Lines[i].strip("\n")
        arr.append(Lines[i].split(' '))
        for j in range(len(arr[i])):
            np.put(matrix[i], [j], arr[i][j])
               
def getMaxSum(matrix, index):
    maxNums = []
    lastIndex = 0
    for i in range(index, int(math.sqrt(matrix.size))):
        row = matrix[i]
        while np.argmax(row) != lastIndex and np.argmax(row) != lastIndex + 1:
            row[np.argmax(row)] = 0
         
        maxNums.append(row[np.argmax(row)])
        lastIndex = np.argmax(row)
    return sum(maxNums)

#indices = [0,1,2]
#for i in range(3, int(math.sqrt(matrix.size)), 3):
#    largest = 0
#    if i == 0:
#        index = 0
#    else:
#        index = indices[len(indices)-1]
#    index1 = index
#    index2 = index
#    largest = matrix[i][index] + matrix[i+1][index] + matrix[i+2][index]
#    for j in range(2):
#        for k in range(j,j+2):
#            for l in range(k,k+2):
#                if matrix[i][index + j] + matrix[i+1][index + k] + matrix[i+2][index + l] > largest:
#                    largest = matrix[i][index + j] + matrix[i+1][index + k] + matrix[i+2][index + l] > largest
#                    index1 = index + j
#                    index2 = index + k
#                    index3 = index + l
#    indices.append(index1)
#    indices.append(index2)
#    indices.append(index3)
#        
#    
#print(indices)
       
#    
#    
#maxNums = []
#lastIndex = 0
#for row in matrix:
#    while np.argmax(row) != lastIndex and np.argmax(row) != lastIndex + 1:
#         row[np.argmax(row)] = 0
#         
#    maxNums.append(row[np.argmax(row)])
#    lastIndex = np.argmax(row)
    
#print(maxNums)
#print(sum(maxNums))
#print(getMaxSum(matrix,0))
    
#maxPos = []
#maxPos.append([0])
#for i in range(int(math.sqrt(matrix.size))):
#    arr = [] 
#    if i < 3:
#        for j in range(i+1):
#            arr.append(j)
#    else:
#        for j in range(3):
#            newMax = np.argmax(matrix[i])
#            arr.append(newMax)
#            matrix[i][newMax] = 0
#    maxPos.append(arr)
#del maxPos[0]    
#
#posMatrix = np.zeros([len(maxPos),3])
#for row in maxPos:
#    for elt in row:
#        np.put(posMatrix[maxPos.index(row)], row.index(elt), elt)
#
#
#final = [0]
#for row in range(1, len(maxPos)-2, 3):
#    largestSum = 0
#    element = 0
#    for val in maxPos[row]:
#        if final[row-1] == val or final[row-1] == val + 1:
#            a = matrix[row][val] + matrix[row+1][val] + matrix[row+2][val]
#            b = matrix[row][val] + matrix[row+1][val + 1] + matrix[row+2][val + 1]
#            c = matrix[row][val] + matrix[row+1][val + 1] + matrix[row+2][val + 2]
#            if a > largestSum:
#                largestSum = a
#                element = val
#            if b > largestSum:
#                largestSum = b
#                element = val
#            if c > largestSum:
#                largestSum = c
#                element = val
#    final.append(element)
#for row in range(len(maxPos) - 2, len(maxPos)):
#    final.append(np.argmax(matrix[row]))
#    
#print(final)
#total = 0
#for i in range(len(final)):
#    total += matrix[i][final[i]]
#
#print(total)





