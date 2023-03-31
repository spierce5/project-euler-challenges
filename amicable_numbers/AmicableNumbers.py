# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:11:47 2021

@author: Sam
"""

import math

divisors = {}
amicable = set()

def getDivisors(n):
    if n in divisors:
        return divisors[n]
    else:
        div = set()
        div.add(1)
        for i in range(int(math.sqrt(n) + 1), 1, -1):
            if i not in div:
                if n % i == 0:
                    div.add(i)
                    div.add(n//i)
        divisors[n] = div
        return div
                    
def isAmicable(a):
    if a in amicable:
        return True
    else:
        da = sum(getDivisors(a))
        db = sum(getDivisors(da))
        if a == db and a != da:
            amicable.add(a)
            amicable.add(da)
            return True
        else:
            return False
    
for i in range(2,10000):
    isAmicable(i)

print(sum(amicable))
    
    
    
    
    
    
    
    
    
    