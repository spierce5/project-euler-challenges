# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 02:04:31 2020

@author: Sam
"""

import math
import time

# A method to calculate perfect squares up to the square root of n
def getSquares(n):
    squares = []
    for i in range(2, math.floor(math.sqrt(n))):
        squares.append(math.pow(i,2))
    return squares

#A method to calculate cubes up to the cube root of n
def getCubes(n):
    cubes = []
    for i in range(2, math.floor(math.pow(n, 1/3))):
        cubes.append(math.pow(i,3))
    return cubes

def checkPalindrome(n):
    num1 = str(int(n))
    num2 = num1[::-1]
    if num1 == num2:
        return True
    else:
        return False
    
def inside(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return True
  
    # If we reach here, then the element was not present 
    return False
        

tic = time.perf_counter()

b = 800000000
squares = getSquares(b)
cubes = getCubes(b)
palindromes = {}
Solutions = []

for x in squares:
    for y in cubes:
        if checkPalindrome(x + y):
                if int(x + y) in palindromes:
                    n = palindromes.get(x + y)
                    n += 1
                    palindromes[int(x + y)] = n
                else: 
                    palindromes[int(x + y)] = 1
                    
for key in palindromes:
    if palindromes.get(key) == 4:
        Solutions.append(key)
        
toc = time.perf_counter()
print(toc-tic)
print(Solutions)
print(sum(Solutions))
    





