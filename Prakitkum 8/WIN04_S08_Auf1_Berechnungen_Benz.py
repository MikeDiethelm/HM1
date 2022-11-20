# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 15:29:48 2022 

@author: Benssy
"""

from scipy.linalg import qr
import numpy as np 

#--------------------------------------------
#exercise a)
Matrix_A = np.array([[1,-2,3],[-5,4,1],[2,-1,3]])
q,r= qr(Matrix_A)
q1= np.array([[-0.182574186,0.9128709292,-0.3651483717],[0.9128709292,0.295322574,0.2818709704],[-0.3651483717,0.2818709704,0.8872516118]])
q2= np.array([[1,0,0],[0,-0.6902,0.7236],[0,0.7236,0.6909]])
q1a=np.array([[-5.477,4.382,-0.730],[0,-0.926,3.880],[0,0.9705,1.848]])
q1t= np.array([[-0.182574186,0.9128709292,-0.3651483717],[0.9128709292,0.295322574,0.2818709704],[-0.3651483717,0.2818709704,0.8872516118]]).transpose()
q2t= q2= np.array([[1,0,0],[0,-0.6902,0.7236],[0,0.7236,0.6909]]).transpose()
q = np.array([[-0.1826,-0.8943,0.4083],[0.9129,0,0.4084],[-0.3651,0.4475,0.8170]])
v2= np.array([[-2.267,0.9705]]).transpose()
v2t= np.array([[-2.267,0.9705]])

print(Matrix_A)
print("QR python")
print(q,r)
print("Q1*A manuell")
print(np.matmul(q1,Matrix_A))
print("v2 * v2t")
print(np.matmul(v2,v2t))
print("v2")
print(v2)
print("v2t")
print(v2t)
print("v2t * v2")
print(np.matmul(v2t,v2))
print("Q2*Q1A")
print(np.matmul(q2,q1a))
print("q1t*a2t = q:")
print(np.matmul(q1t,q2t))
#-------------------------------------------
#exercise b)
qt=np.array([[-0.1826,-0.8943,0.4083],[0.9129,0,0.4084],[-0.3651,0.4475,0.8170]]).transpose()
b = np.array([[1,9,5]]).transpose()
print(b)
print("Qt*b:")
print(np.matmul(qt,b))




