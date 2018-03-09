# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 08:04:47 2018

@author: jrbrad
"""

import sys, threading

sys.setrecursionlimit(800000)
threading.stack_size(100000000) #67108864

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

def main():
    print(factorial(1000))

thread = threading.Thread(target=main)
thread.start()