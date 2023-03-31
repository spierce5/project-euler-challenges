# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:26:18 2020

@author: Sam
"""
import math

nums = []
with open('C:/Users/Sam/Desktop/Current_Scripts/Python_Scripts/ProjectEuler/TextFiles/largeSum.txt','r') as fp:
    Lines = fp.readlines()
    for line in Lines:
        nums.append(int(line)/math.pow(10,40))
        

totalSum = 0
for x in nums:
    totalSum += x
    
while totalSum > 9999999999:
    totalSum /= 10
    
print(math.floor(totalSum))