# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:10:12 2022

@author: Benssy
"""

import numpy as np 
from scipy.special import jacobi 
import math as m

Matrix_A= np.array([[0,-5/8,-1/4],[-5/9,0,-1],[-4/7,-2/7,0]])
x = np.array([[0,0,0]]).transpose()
x_1 =np.array([[19/8,5/9,34/7]]).transpose()
x_2_1 = Matrix_A @ x_1
x_2 = x_2_1 + x_1

print('x2_1', x_2_1)
print('x2',x_2)

print("Jacobi")
def Jacobi(A,b,x,steps):
    L = np.tril(A,k=-1)
    D = np.diag(np.diag(A))
    R = np.triu(A, k=1)
    for steps in range(steps):
        print('x',x)
        x = -np.linalg.inv(D) @ (L + R) @ x + np.linalg.inv(D) @ b
        B = -np.linalg.inv(D) @ (L + R)
        print ('B',B)
    return x

A = np.array([[8,5,2],[5,9,1],[4,2,7]])
b = np.array([[19],[5],[34]])
x = np.array([[1],[-1],[3]])
steps = 3
print(Jacobi(A,b,x,steps))

print('log', m.log10(7.96*10**-6)/m.log10(0.875))
