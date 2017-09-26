# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:35:47 2017

@author: Le
"""

import numpy as np
import math

n=input("Please enter value for n: ")
m=float(n)
o=int(n)
def factorial(m):
    if m == 0:
        return 1
    else:
        return m*factorial(m-1)
def factorial(o):
    if o == 0:
        return 1
    else:
        return o*factorial(o-1)

print('Float: {}' .format(factorial(m)))
print('Integer: {}' .format(factorial(o)))
print('It can be seen that n=170 is the last value where the float variant will give a non-infinity answer. This suggests that there is a limit to the number of digits the float variant can store a certain number of digits, whereas the integer variant stores all of the digits.')