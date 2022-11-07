# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 08:58:06 2022

@author: adria
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def findXVector(A,b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = 0
    while round < x_dim:
        print(b[round][0])
        print(A[round][round])
        b[round][0] = b[round][0] / A[round][round]
        round +=1
    print(b)

def jordan(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = x_dim-1
    while round >= 0:
        nextLine = round-1
        while nextLine >= 0:
            print(nextLine)
            print(round)
            print("Matrix Value")
            print(A[nextLine][round])
            print(A[round][round])
            divideBy = A[nextLine][round] / A[round][round]
            print(divideBy)
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            for item in range(y_dim):
                print("Item range")
                print(A)
                print(A[nextLine][item])
                print(A[round][item])
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
                print(A)
            nextLine = nextLine -1
        round = round -1
    print("result jordan: ")
    print(A)
    print(b)
    findXVector(A, b)

def gaus(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    #print("x-Dimension ") 
    #print(x_dim)
    #print("y-dimension ")
    #print(y_dim)
    round = 0
    while round <= x_dim:
        nextLine = round +1
        while nextLine <= x_dim-1:
            #print(round)
            #print(nextLine)
            #print(A[nextLine][round])
            #print(A[round][round])
            divideBy = A[nextLine][round] / A[round][round]
            #print("division")
            #print(divideBy)
            #print(nextLine)
            #print(divideBy)
            #print(b[nextLine][0])
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            #print(b[nextLine][0])
            for item in range(y_dim):
                #print("new item")
                #print(item)
                #print(nextLine)
                #print(round)
                #print(A[nextLine][item])
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
                #print(A[nextLine][item])
            
            nextLine = nextLine +1
        round = round +1
    print("Result: ")
    print(A)
    print(b)
    jordan(A, b)
 
    
    
def startMethod():
    Matrix_A = np.array([[2,7,3],[-4,-10,0],[12,34,9]])
    Vector_b = np.array([[5,-22,42]])
    Vector_b = np.transpose(Vector_b)
    print("Start matrix: ")
    print(Matrix_A)
    print("start B: ")
    print(Vector_b)
    gaus(Matrix_A, Vector_b)

startMethod()