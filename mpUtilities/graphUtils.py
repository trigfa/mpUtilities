# -*- coding: utf-8 -*-
"""
A number of useful functions for dealing with graphs

Created on Sun Dec  8 17:46:29 2013

@author: Graham
"""

import numpy as np
import scipy
import scipy.interpolate
import sys

def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = np.arange(len(v))
    
    v = np.asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not np.isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = np.Inf, -np.Inf
    mnpos, mxpos = np.NaN, np.NaN
    
    lookformax = True
    
    for i in np.arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return np.array(maxtab), np.array(mintab)

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
    
def interpolate_data(xarray, yarray, minvalue, maxvalue):
    interpx=np.linspace(minvalue,maxvalue, 201)
    interpy=scipy.interpolate.interp1d(xarray, yarray)(interpx)
    return interpx, interpy