# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 01:43:28 2021

@author: Sam
"""

passcode = ''
preceding = {}


with open(r'C:\Users\Sam\Desktop\Current_Scripts\Python_Scripts\ProjectEuler\TextFiles\keylog.txt', 'r') as fp:
    Lines = fp.readlines()
    for line in Lines:
        line.strip('\n')
        if line[0] not in preceding:
            preceding[line[0]] = set()
        if line[1] not in preceding:
            preceding[line[1]] = {line[0]}
        else: 
            preceding.get(line[1]).add(line[0])
        if line[2] not in preceding:
            preceding[line[2]] = {line[0], line[1]}
        else:
            preceding.get(line[2]).update([line[0], line[1]])
            
for i in range(len(preceding)):
    for elt in preceding:
        if len(preceding.get(elt)) == i:
            passcode += elt
            
print(passcode)
        

