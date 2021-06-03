# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:18:03 2020

@author: Sam
"""

from num2words import num2words

numLetters = 0
for i in range(1, 1001):
    word = num2words(i)
    for char in word:
        if char.isalpha():
            numLetters += 1
            
print(numLetters)
