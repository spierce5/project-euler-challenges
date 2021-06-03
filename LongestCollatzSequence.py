# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:47:26 2020

@author: Sam
"""

chainLengths = {1:1}

# This method could be improved by utilizing chainLengths, but I like how it passes the length through and
# uses a default argument

#def getSeqLength(n,length=1):        #length=1 is default value
#    if n == 1:
#        return length
#    elif n in chainLengths:
#        return chainLengths[n]
#    else: 
#        if n % 2 == 0:
#            return getSeqLength(n//2, length + 1)
#        else: 
#            return getSeqLength((3 * n) + 1, length + 1)

def getSeqLength(n):
    if n < 1:
        return None
    if n in chainLengths:
        return chainLengths[n]
    else:
        if n % 2 == 0:
            chainLengths[n] = 1 + getSeqLength(n//2)
            return chainLengths[n]
        else: 
            chainLengths[n] = 1 + getSeqLength((3 * n) + 1)
            return chainLengths[n]
        
longestChain = 0
startingNum = 0
for i in range(1, 1000000):
    temp = getSeqLength(i)
    if temp > longestChain:
        longestChain = temp
        startingNum = i
        
print('The Collatz sequence of ', startingNum, ' has ', longestChain, ' terms')
