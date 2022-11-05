# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:37:13 2022

@author: Benssy
"""

#Teillösung von Adel für Aufg2

import numpy as np

def gaus(A,b):
    n = np.shap(A)[0]
    M = np.zeros((n,n+1))
    M[0:n,0:n]= np.copy(A)
    M[0:n,n] = np.copy(b)
    
    return (M,x)