# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:29:48 2022

@author: benss
"""

from Witschi_Florian_S6_Aufg2 import *
import numpy as np
import math
import matplotlib.pyplot as plt

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



""" print("Original Matrix A:")
print(A)
print("Original Vector b:")
print(b) """
#[A_triangle,detA,x] = Witschi_Floian_S6_Aufg2(A,b)
#[A_triangle,detA,x] = Witschi_Floian_S6_Aufg2(A_one,b_one) 
[A_triangle,detA,x] = Witschi_Floian_S6_Aufg2(A_two,b_two) 
#[A_triangle,detA,x] = Witschi_Floian_S6_Aufg2(A_three,b_three)
#[A_triangle,detA,x] = Witschi_Floian_S6_Aufg2(A_four,b_four) 
print("Upper triangle matrix:")
print(A_triangle)
print("Solution matrix x:")
print(x)
print("Determinant:")
print(detA)
print("***FOLLOWING PARAMETERS WITH NUMPY")
y = np.linalg.solve(A_two, b_two)
print(y)

#Die Lösungsmatrix ist folgende (Für die A_four):
""" Solution matrix x:
[[ 1.00000000e+00]
 [-1.00000000e+00]
 [ 5.16758353e-14]
 [ 2.00000000e+00]
 [ 3.00000000e+00]
 [ 3.00000000e+00]
 [-8.00000000e+00]
 [ 1.50000000e+01]]
Der 3. WErt mit 5-14 sollte eigenlich 0 sein und ist vermutlich der Maschinenungenauigkeit geschuldet """