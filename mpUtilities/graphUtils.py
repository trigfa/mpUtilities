# -*- coding: utf-8 -*-
"""
A number of useful functions for dealing with graphs

Created on Sun Dec  8 17:46:29 2013

@author: Graham
"""

import numpy as np
import scipy
import scipy.interpolate

def derivative(x,y):
    dy=y[1:]-y[:-1]
    dx=x[1:]-x[:-1]    
    dy_dx = dy/dx
    centre_x = (x[1:]+x[:-1])/2.0
    return centre_x, dy_dx
    
def normalise_to_x0(xarray,yarray):
    """Given an xarray and yarray returns an array which is normailsed to 100% at xarray=0""" 
    xzero=(np.where(xarray==(find_nearest(xarray, 0))))
    yzero=yarray[xzero]
    ynorm = (yarray/yzero)*100
    return ynorm

def normalise_to_max(xarray,yarray):
    """Given an xarray and yarray returns an array which is normailsed to 100% at the maximum value of yarray""" 
    ymax=max(yarray)
    ynorm = (yarray/ymax)*100
    return ynorm
    
def find_nearest(array,value):
    idx=(np.abs(array-value)).argmin()
    return array[idx]
    
def interpolate_data(xarray, yarray, minvalue, maxvalue):
    interpx=np.linspace(minvalue,maxvalue, 201)
    interpy=scipy.interpolate.interp1d(xarray, yarray)(interpx)
    return interpx, interpy