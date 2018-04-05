# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx


data = np.full((15,3),np.nan)
duplicates = True
while duplicates == True:
    data[0:5,0] = (np.random.randint(0,20,(5)))
    data[0:5,1] = (np.random.randint(0,20,(5)))
    data[5:10,0] = (np.random.randint(30,50,(5)))
    data[5:10,1] = (np.random.randint(0,20,(5)))
    data[10:15,0] = (np.random.randint(15,30,(5)))
    data[10:15,1] = (np.random.randint(30,50,(5)))
    if len(np.unique(data[:,:2], axis = 0)) < len(data):
        duplicates = True
    else:
        duplicates = False



for i in range(len(data)):
    data[i,2] = find_nearest(data[centres,:2],data[i,:2])

plt.scatter(data[:,0],data[:,1],c=data[:,2])

duplicates = True
while duplicates == True:
    centres = np.random.randint(0,15,3)
    if len(np.unique(data[:,:2], axis = 0)) < len(data):
        duplicates = True
    else:
        duplicates = False

for i in range(len(data)):
    data[i,2] = find_nearest(data[centres,:2],data[i,:2])

print(len((data)))

