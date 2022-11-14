# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 06:55:29 2022

@author: Benssy
"""
from scipy.linalg import lu
import numpy as np


Matrix_A = np.array([[0.8,2.2,3.6],[2.0,3.0,4.0],[1.2,2.0,5.8]])
Vector_b = np.array([[2.4, 1.0, 4.0]])
Vector_b = np.transpose(Vector_b)
p,l,u = lu(Matrix_A)

print(p,l,u)

#Answer: same as in "written form"