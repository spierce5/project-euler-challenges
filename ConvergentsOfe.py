# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:02:00 2020

@author: Sam
"""

import fractions as fr

terms = {}

# Method to calculate nth term of sqrt(2)
#def getTerm(n, frac = fr.Fraction(2,1)):
#    if n == 1: 
#        return frac - 1
#    else:
#        frac = 2 + fr.Fraction(1,frac)
#        return getTerm(n-1, frac)

# Method to calculate nth term of e 
def getTerm(n, frac = fr.Fraction(1,2), first = True):
    if first:
        first = False
        if n < 4:
            if n == 1:
                return 2
            elif n == 2:
                return 3
            else:
                return fr.Fraction(8,3)
        elif (n - 1) % 3 == 0:
            k = (n - 1) // 3
            frac = fr.Fraction(1, (2 * k) + 1)
        elif n % 3 == 0:
            k = n // 3
            frac = fr.Fraction(1, (2 * k))
            frac = fr.Fraction(1, 1 + frac)
            
        
    if n == 3:
        frac = 2 + frac
        return frac
    elif (n + 1) % 3 == 0:
        k = ((n + 1) // 3) - 1
        frac = fr.Fraction(1, (2 * k) + frac)
        return getTerm(n-1, frac, first)
    else:
        frac = fr.Fraction(1, 1 + frac)
        return getTerm(n-1, frac, first)

#print(getTerm(9))

ratio = getTerm(100)
numerator = ratio.numerator
s = str(numerator)
num = 0
for digit in s:
    num += int(digit)
    
print(num)

