# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:17:55 2022

@author: Benssy
"""

import numpy as np

def sekanten(f,x0,x1,tol):
    y = np.exp(x1**2)+x1**-3-10 #f(x1)
    x = np.exp(x0**2)+x0**-3-10 #f(x0)
    z = y -x
    x3= x1-((x1-x0)/z)
    return round(x3,tol)

#example
def f(x):
    
    return np.exp(x**2)+x**-3-10

print(sekanten(1, -1.5, -1, 4))
