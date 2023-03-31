# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:29:44 2021

@author: Sam
"""

import csv

def abcAppend(s, lst):
    found = False
    for i in range(len(lst)):
        if s < lst[i]:
            found = True
            lst.insert(i,s)
            break
    if not found:
        lst.append(s)
        
def getAlphaValue(s):
    total = 0
    for char in s:
        total += int(ord(char) - 64)
    return total
        
names = []
with open(r'C:\Users\Sam\Desktop\Current_Scripts\Python_Scripts\ProjectEuler\TextFiles\names.txt', 'r') as fp:
    csv_reader = csv.reader(fp, delimiter=',')
    for row in csv_reader:
        for item in row:
            abcAppend(item, names)
    
grandTotal = 0
for i in range(len(names)):
    grandTotal += (i+1) * getAlphaValue(names[i])
    
print(grandTotal)