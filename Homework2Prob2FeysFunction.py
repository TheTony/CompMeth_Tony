# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:57:13 2017

@author: Le
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt,sin,cos,pi 
from numpy import empty,zeros
from pylab import imshow,gray,show

theta=np.arange(0,24*np.pi,0.01)
r=np.e**(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5
x=r*np.cos(theta)
y=r*np.sin(theta)
ax = plt.subplot(projection='polar')
ax.plot(theta,r)
ax.set_rticks([1,2, 3, 4, 5,6])  # less radial ticks
ax.set_rlabel_position(90)  # get radial labels away from plotted line
ax.grid(True)
plt.show()

bx = plt.subplot()
bx.plot(x,y)
plt.show()  