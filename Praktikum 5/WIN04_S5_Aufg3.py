# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:17:55 2022

@author: Benssy
"""

import numpy as np

def sekanten(f,x0,x1,tol):
    y= f(x1)-f(x0)
    x3= x1-((x1-x0)/y)
    round(x3,tol)
    return x3

#example
def f(x):
    return np.exp(x**2)+x**-3-10

print(sekanten(1, -1.5, -1, 4))