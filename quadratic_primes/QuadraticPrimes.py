# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:31:16 2021

@author: Sam
"""

#Sieve of Eratosthenes
primes = set(range(2, 100000))  
p = 2
while p < 100:
    if p in primes:
        for q in range(2, 100000 // p + 1):
            primes.discard(p * q)
    p += 1

products = {}

for a in range(-1000,1000):
    for b in range(-1000,1000):
        if (a,b) not in products:
            products[(a,b)] = set()
        n = 0
        while (n**2 + a*n + b) in primes and n < b:
            products[(a,b)].add(n**2 + a*n + b)
            n += 1
            
result = ()
mostPrimes = 0
for item in products:
    if len(products.get(item)) > mostPrimes:
        mostPrimes = len(products.get(item))
        result = item
        
print(result[0] * result[1])
    
    
        
