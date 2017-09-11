# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:22:28 2017

@author: Le
"""

#Problem 5 Quantum potential step
EE=10
VE=9
hb=6.582e-16
mm=(9.11e-31)*((2.997e8)**2)/(1.783e-36)
k1=np.sqrt(2*mm*EE)/hb
k2=np.sqrt(2*mm*(EE-VE))/hb
TT=(4*k1*k2)/(k1+k2)**2
RR=((k1-k2)/(k1+k2))**2
print(TT)
print(RR)
print(TT+RR)
