# -*- coding: utf-8 -*-
"""
A number of useful functions for dealing with graphs

Created on Sun Dec  8 17:46:29 2013

@author: Graham
"""

import numpy as np
import scipy
import scipy.interpolate

def derivative(x,y,order=1):
    """Given the x any y arrays will return the derivative of this array, optionally higher derivatives
    can be calculated by giving the order"""
    for n in range(1,order+1,1):
        dy=y[1:]-y[:-1]
        dx=x[1:]-x[:-1]    
        y = dy/dx
        x = (x[1:]+x[:-1])/2.0
    return x, y
    
def normalise_to_x0(xarray,yarray):
    """Given x and y arrays returns a y array which is normailsed to 100% at xarray=0""" 
    xzero=(np.where(xarray==(find_nearest(xarray, 0))))
    yzero=yarray[xzero]
    ynorm = (yarray/yzero)*100
    return ynorm

def normalise_to_max(xarray,yarray):
    """Given x and y arrays returns a y array which is normailsed to 100% at the maximum value of the original y array""" 
    ymax=max(yarray)
    ynorm = (yarray/ymax)*100
    return ynorm
    
def find_nearest(array,value):
    """Finds the vlaue nearest to that given in an array"""
    idx=(np.abs(array-value)).argmin()
    return array[idx]
    
def interpolate_data(xarray, yarray, minvalue, maxvalue, length=201):
    interpx=np.linspace(minvalue,maxvalue, length)
    interpy=scipy.interpolate.interp1d(xarray, yarray)(interpx)
    return interpx, interpy