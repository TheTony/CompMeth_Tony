# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:08:07 2017

@author: Le
"""

import numpy as np
import math as m


#Problem 10 The semi-empirical mass formula
a1=15.67
a2=17.23
a3=0.75
a4=93.2
#ZZ=int(input("enter Z value: "))
#AA=int(input("enter A value: "))
ZZ=1
EAmax=0
AAmax=0
ZZmax=0
while(ZZ<11):
    AA=ZZ
    AA2=AA    
    EB=0
    while(AA<(3*ZZ)):
        test = AA % 2
        test2 = ZZ % 2

        if(test==1):
            a5=float(0)
            print(AA,ZZ,"ZERO") #Used to test if zero triggers
        elif(test==0):
            if(test2==0):
                a5=float(12)
                print(AA,ZZ,"POS") #Used to test if 12 triggers
            elif(test2==1):
                a5=float(-12)
                print(AA,ZZ,"NEG") #Used to test if -12 triggers
                
        EB1=a1*AA - a2*AA**(2/3) - (a3/(AA**(1/3)))*(ZZ**2) - (a4/AA)*((AA-2*ZZ)**2) + a5/np.sqrt(AA)
        if(EB<EB1):
            EB=EB1
            AA2=AA
        AA=AA+1
        
    EA=EB/AA2
    
    if(EAmax<EA):
        EAmax=EA
        AAmax=AA2
        ZZmax=ZZ
        
    print(ZZ,AA2,a5,EA)
    ZZ=ZZ+1
    
print(ZZmax,AAmax,EAmax)