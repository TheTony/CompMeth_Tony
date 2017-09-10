# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:08:07 2017

@author: Le
"""

import numpy as np
import math as m

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

#Problem 10 The semi-empirical mass formula
a1=15.67
a2=17.23
a3=0.75
a4=93.2
#ZZ=float(input("enter Z value: "))
#AA=float(input("enter A value: "))
ZZ=1
EAmax=0
AAmax=0
ZZmax=0
while(ZZ<100):
    AA=ZZ
    test = AA % 2
    test2 = ZZ % 2

    if(test==1):
        a5=float(0)    
    elif(test==0):
        if(test2==1):
            a5=float(12)
        elif(test2==0):
            a5=float(-12)
        
    EB=0
    while(AA<3*ZZ):
        EB1=a1*AA-a2*AA**(2/3)-a3*(ZZ**2/AA**(1/3))-a4*(((AA-2*ZZ)**2)/AA)+a5/AA**(1/2)
        if(EB<EB1):
            EB=EB1
            AA2=AA
        AA=AA+1
        
    EA=EB/AA2
    
    if(EAmax<EA):
        EAmax=EA
        AAmax=AA2
        ZZmax=ZZ
        
    print(ZZ,AA2,EA)
    ZZ=ZZ+1
    
print(ZZmax,AAmax,EAmax)
    
#EA1=0
#if(EA1<EA):
#    EA1=EA
#print(EA1)