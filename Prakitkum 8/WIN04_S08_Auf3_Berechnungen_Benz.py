# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:45:16 2022

@author: Benssy
"""
import numpy as np

A = np.array([[20,30,10],[10,17,6],[2,3,2]])
b_strich= np.array([[5820,3400,936]]).transpose()
A_inv = np.linalg.inv(np.array([[20,30,10],[10,17,6],[2,3,2]]))

print("x_strich")
print(np.linalg.solve(A, b_strich))
print("A inverse")
print(A_inv)