# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:37:13 2022

@author: Benssy
"""

#Teillösung von Adel für Aufg2

import numpy as np
import math
import matplotlib.pyplot as plt

def gaus(A,b):
    n = np.shape(A)[0]
    M = np.zeros((n,n+1))
    M[0:n,0:n]= np.copy(A)
    M[0:n,0:n] = np.copy(b)
    
    return (M,b)

#test

A = np.array([[-1,1,1],[1,-3,-2],[5,1,4]])
b = np.array([[0,5,3]])
b = b.transpose()
A_one = np.array([[4,-1,-5],[-12,4,17],[32,-10,-41]])
b_one = np.array([[-5,-9,-39]])
b_one = b_one.transpose()
A_two = np.array([[2,7,3],[-4,-10,0],[12,34,9]])
b_two = np.array([[5,-22,42]])
b_two = b_two.transpose()
A_three = np.array([[-2,5,4],[-14,38,22],[6,-9,-27]])
b_three = np.array([[16,82,-120]])
b_three = b_three.transpose()
A_four = np.array([[-1,2,3,2,5,4,3,-1],[3,4,2,1,0,2,3,8],[2,7,5,-1,2,1,3,5],[3,1,2,6,-3,7,2,-2],[5,2,0,8,7,6,1,3],[-1,3,2,3,5,3,1,4],[8,7,3,6,4,9,7,9],[-3,14,-2,1,0,-2,10,5]])
b_four = np.array([[-11,103,53,-20,95,78,131,-26]])
b_four = b_four.transpose()

#[A_triangle,detA,x] = gaus(A_four,b_four) 
print(gaus(A_four,b_four))
print("numpy function")
y = np.linalg.solve(A_four, b_four)
print(y)