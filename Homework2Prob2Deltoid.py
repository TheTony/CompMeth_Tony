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

side = 1000 # Side of the square
points = 100
spacing = side/points # Spacing of points

# Make an array to store the heights
xj = zeros([points,points],float)
yi = zeros([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    #print(y)
    yi[i] = 2*sin(2*np.pi*i*0.1)-sin(4*np.pi*i*0.1)
    #print(yi[i])
    
for j in range(points):
    x = spacing*j
    #print(x)
    xj[j] = 2*cos(2*np.pi*j*0.1)+cos(4*np.pi*j*0.1)
    #print(xj[j])    
    
# Make the plot
plt.plot(xj,yi,color="black")
plt.show()  