# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 08:58:06 2022

@author: Adrian, Mike, Benssy
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy as s

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
    #print("result Jordan: ")
    #print(A)
    #print(b)
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
    
    #print("Result Gauss: ")
    #print(A)
    #print(b)
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

#Aufgabe 2 (startMethod):
startMethod()

#Aufgabe 3 Teste verschiedene Matrizen

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


print("Calculated x Vector:")
print(gaus(np.copy(A), np.copy(b)))
print()
print(np.linalg.solve(A, b))
print("Calculated x Vector:")
print(gaus(np.copy(A_one), np.copy(b_one)))
print()
print(np.linalg.solve(A_one, b_one))
print("Calculated x Vector:")
print(gaus(np.copy(A_two), np.copy(b_two)))
print()
print(s.linalg.solve(A_two, b_two))
print("Calculated x Vector:")
print(gaus(np.copy(A_three), np.copy(b_three)))
print()
print(np.linalg.solve(A_three, b_three))
print("Calculated x Vector:")
print(gaus(np.copy(A_four), np.copy(b_four)))
print()
print(np.linalg.solve(A_four, b_four))

#Aufgabe 3:
#   Die Werte der Dreiecksmatrix unterscheiden sich voneinander, 
#   weil die numpy.linalg.solve die Zeilen der Matrix austauscht,
#   was wir manuell nicht machen. 
#   numpy.linalg.solve tauscht die Zeilen aus, 
#   damit immer der grössere Wert vom kleineren Wert abgezogen wird,
#   um Rechenfehler zu vermeiden.