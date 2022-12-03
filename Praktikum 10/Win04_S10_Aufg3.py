# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:13:48 2022 

@author: Adrian, Benssy, Mike
"""

from Win04_S10_Jacobi import jacobiVerfahren

def gaussSeidelVerfahren(A, b, x0, tol):
    return "Resultat"

def startPoint(A, b, x0, tol, opt):
    if(opt == "J"):
        return jacobiVerfahren(A, b, x0, tol)
    elif(opt == "GS"):
        return gaussSeidelVerfahren(A, b, x0, tol)
    else:
        print("Option nicht bekannt") 
        print(opt)