# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 08:07:35 2018

@author: jrbrad
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(2000))