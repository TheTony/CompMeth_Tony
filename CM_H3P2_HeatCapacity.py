# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:23:50 2017

@author: Le
"""
import numpy as np
import math
from numpy import ones,copy,cos,tan,pi,linspace
import matplotlib.pyplot as plt


T1=5
t2=500 

V=1000/((10**2)**3)        #m^3                    #volume
rho=6.022*10**28           #m^-3                   #number density of atoms
Del=428                    #K                      #Debye Temperature            
kB

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))
    
    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def CvINT(x):
    return (x**4*math.e**4)/(math.e**x-1)**2

Cv=np.array([])
Temp=np.array([])
for T in range(5,501):
    const=9*V*rho*kB*(T/Del)**3
    pts,weights=gaussxwab(50,0,Del/T)
    Cv=np.append(Cv,np.sum(const*weights*CvINT(pts)))
    Temp=np.append(Temp,T)

ax=plt.subplot()
ax.plot(Temp,Cv)
print(Cv,Temp)



