# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:56:21 2020

@author: Sam
"""

months = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 
          'Oct':31, 'Nov':30, 'Dec':31}

count = 0
currentDay = 2                  #01/01/1901 was Tuesday
for year in range(1901, 2001):
    for month in months:
        days = months.get(month) + 1
        if month == 'Feb':
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29 + 1
        for day in range(1,days):
            if day == 1 and currentDay % 7 == 0:
                count += 1
            currentDay += 1
        
print(count)