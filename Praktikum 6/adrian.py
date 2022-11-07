# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 08:58:06 2022

@author: adria
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def findXVector(A,b):
    round = 0
    while round < A.shape[0]:
        b[round][0] = b[round][0] / A[round][round]
        round +=1
    
    return b

def jordan(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = x_dim-1
    while round >= 0:
        nextLine = round-1
        while nextLine >= 0:
            divideBy = A[nextLine][round] / A[round][round]
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            for item in range(y_dim):
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
            nextLine = nextLine -1
        round = round -1
    print("result Jordan: ")
    print(A)
    print(b)
    return findXVector(A, b)

def gaus(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = 0
    while round <= x_dim:
        nextLine = round +1
        while nextLine <= x_dim-1:
            divideBy = A[nextLine][round] / A[round][round]
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            
            for item in range(y_dim):
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
            nextLine = nextLine +1
        round = round +1
    
    print("Result Gauss: ")
    print(A)
    print(b)
    return jordan(A, b)
 
    
    
def startMethod():
    Matrix_A = np.array([[2,7,3],[-4,-10,0],[12,34,9]])
    Vector_b = np.array([[5,-22,42]])
    Vector_b = np.transpose(Vector_b)
    print("Start matrix: ")
    print(Matrix_A)
    print("start B: ")
    print(Vector_b)
    foundX = gaus(Matrix_A, Vector_b)
    print("Calculated x Vector:")
    print(foundX)

startMethod()