# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:48:09 2020

@author: Sam
"""
import math
from itertools import permutations

#endValue = {1:1,10:1,13:1,32:1,44:1,85:89,89:89,145:89,42:89,20:89,4:89,16:89,37:89,58:89}
endValue = {1:1,89:89}
squareDigits = {1:1}
anagrams = {}

def getDigits(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    return digits

def getPerms(n):
    if n in anagrams:
        return anagrams[n]
    else:
        perm = permutations(getDigits(n))
        result = []
        for arr in perm:
            num = ''
            for digit in arr:
                num += str(digit)
            result.append(int(num))
        for num in result:
            anagrams[int(num)] = result
    return result
        
def getSquareDigit(n):
    if n == 1:
        return 1
    elif n in squareDigits:
        return squareDigits[n]
    else:
        s = 0
        for digit in getDigits(n):
            s += int(math.pow(digit,2))
        for perm in getPerms(n):
            squareDigits[int(perm)] = s
        return s
    
def getChain(n, chain = []):
    if n in endValue:
        for num in chain:
            perms = getPerms(num)
            for perm in perms:                
                endValue[perm] = endValue.get(n)
        chain.clear()
        return None
    else:
        chain.append(n)
        return getChain(getSquareDigit(n), chain)
    
#for i in range(1, 10000000):
#    if i not in endValue:
#        getChain(i)
##
##for i in range(1,10000000):
##    getChain(i)
##    
#count = 0
#for item in endValue:
#    if item < 10000000 and endValue.get(item) == 89:
#        count+=1
#    
#print(count)
#        
#count = 0
#for i in range(1, 568 ):
#    if i not in endValue.keys():
#        chain = getChain(i)
#        if endValue.get(i) == 89:
#            count += len(anagrams[i])
#         
#print(count)

#seqTo89 = []
#for i in range(1,568):
#    getChain(i)
#    if endValue.get(i) == 89:
#        seqTo89.append(i)
        
#count = 0
#for num in seqTo89:
#    checked = []
#    if num <= 81:
#        root = int(math.sqrt(num))
#        for i in range(10000000,1,-1):
#            if i not in checked:
#                digits = getDigits(i)
#                digits.sort()
#                if digits[len(digits)-1] <= root:
#                    if getSquareDigit(i) == num:
#                        perms = getPerms(i)
#                        checked.extend(perms)
#                        count += len(perms)
#        
#
#print(count)

#sets = {}
#for i in range(1,10000000):
#    sd = getSquareDigit(i)
#    if sd in sets:
#        sets[sd].append(i)
#    else:
#        sets[sd] = [i]
#
#print(sets)














        
        
        