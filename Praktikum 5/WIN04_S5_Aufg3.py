# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:17:55 2022

@author: Benssy
"""

import numpy as np
import math

def sekanten(f,x0,x1,tol):
    xn = x1
    xprev = x0
    while abs(xprev - xn) > tol and abs(xprev-xn) != 0:
        xnew = xn-(((xn-xprev)/(f(xn)-f(xprev)))*f(xn))
        xprev = xn
        xn = xnew
        print(xnew)
    return xnew

#exercise 1
def f(x):
    return np.exp(x**2)+x**-3-10

#exercise 2
def g(x):
    return x-((-(1/3)*math.pi*(x**3))+(5*math.pi*(x**2)-471))

print("Exercise 1")
print(sekanten(f,-1.0, -1.2, 0.0001))
print("Exercise 2")
print(sekanten(g, 9, 7.658, 0.0001))  

#Fazit: Das Sekantenverfahren ist gegenüber dem Newton-Verfahren einfacher darzustellen, 
        #da die Ableitung nicht mitgeliefert werden muss.  
