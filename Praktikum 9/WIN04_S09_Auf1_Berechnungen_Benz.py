# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:50:06 2022

@author: Benssy
"""

import numpy as np
from scipy.linalg import norm

A = np.array([[1,0,2],[0,1,0],[0.0001,0,0.0001]])
b= np.array([[1,1,0]]).transpose()
b_strich= np.array([[1,1,1.667*10**-7]]).transpose()
A_inv = np.linalg.inv(np.array([[1,0,2],[0,1,0],[0.0001,0,0.0001]]))
cond_A = norm(A,np.inf)*norm(A_inv,np.inf)

print("x")
print(np.linalg.solve(A, b))
print("A inverse")
print(A_inv)
print('cond norm A:',cond_A)
print('x_strich',np.linalg.solve(A, b_strich))

#exercise c)
x =np.array([[-1,1,1]]).transpose()
x_strich= np.array([[-0.996,1,0.998]]).transpose()
print ('norm',norm(x - x_strich, np.inf))
print('norm x',norm(x,np.inf))
print(norm(x - x_strich, np.inf)/norm(x,np.inf))

#exercise d)
A_strich = np.array([[1+10**-7,0+10**-7,2+10**-7],[0+10**-7,1+10**-7,0+10**-7],[0.0001+10**-7,0+10**-7,0.0001+10**-7]])
print('norm A_Strich-A',norm(A_strich-A,np.inf))