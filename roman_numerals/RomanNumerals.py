# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 19:23:42 2020

@author: Sam
"""
romanNumerals = {}
numericalValues = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

# Method to get the most efficient roman numeral for a given integer
def getRomanNumeral(n):
    if n in romanNumerals:
        return romanNumerals[n]
    else:
        
        temp = n
        numeral = ''
        while (temp / 1000) >= 1:
            numeral += 'M'
            temp -= 1000
        if (temp / 900) >= 1:
            numeral += 'CM'
            temp -= 900
        if (temp / 500) >= 1:
            numeral += 'D'
            temp -= 500
        if (temp / 400) >= 1:
            numeral += 'CD'
            temp -= 400
        while (temp / 100) >= 1:
            numeral += 'C'
            temp -= 100
        if (temp / 90) >= 1:
            numeral += 'XC'
            temp -= 90
        if (temp / 50) >= 1:
            numeral += 'L'
            temp -= 50
        if (temp / 40) >= 1:
            numeral += 'XL'
            temp -= 40
        while (temp / 10) >= 1:
            numeral += 'X'
            temp -= 10
        if (temp / 9) >= 1:
            numeral += 'IX'
            temp -= 9
        if (temp / 5) >= 1:
            numeral += 'V'
            temp -= 5
        if (temp / 4) >= 1:
            numeral += 'IV'
            temp -= 4
        for i in range(temp):
            numeral += 'I'
        
        romanNumerals[n] = numeral
        return numeral

# Method to get the numerical value of a string containing a roman numeral
def getNumber(s):
    subRule = False                     #used to determine if value second value of a subtractive pair
    num = 0
    for idx, char in enumerate(s):
        if subRule:
            subRule = False
        elif idx < len(s) - 1:
            nextChar = s[idx + 1]
            if numericalValues[char] < numericalValues[nextChar]:
                num += numericalValues[nextChar] - numericalValues[char]
                subRule = True
            else:
                num += numericalValues[char]
        else:
            num += numericalValues[char]
    return num

charSaved = 0
with open(r'C:\Users\Sam\Desktop\Current_Scripts\Python_Scripts\ProjectEuler\TextFiles\roman.txt','r') as fp:
    Lines = fp.readlines()
    for line in Lines:
        line = line.rstrip('\n')
        shortest = getRomanNumeral(getNumber(line))
        if len(line) > len(shortest):
            charSaved += len(line) - len(shortest)

print(charSaved)















