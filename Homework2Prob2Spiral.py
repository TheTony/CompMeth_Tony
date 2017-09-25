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

r=np.arange(0,10*np.pi,0.01)
theta=np.sqrt(r)
x=r*np.cos(theta)
y=r*np.sin(theta)
ax = plt.subplot()
ax.plot(x,y)
    
plt.show()  