# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:13:48 2022 

@author: Adrian, Benssy, Mike
"""

import numpy as np

def jacobiVerfahren(A, b, x0, tol):
    
    division = divideByDiagonal(addBToA(A, b))
    

    b = getBFromAB(division)
    calcA = getAWithoutB(division)

    loes = calcSecondX(calcA, b, b)
    print(loes)
    return loes

def addBToA(A, b):
    newArray = np.zeros((A.shape[0], A.shape[1]+1))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]+1):
            if j < A.shape[1]:
                if i == j: #Schaut ob wir auf der Diagonale sind oder nicht.
                    newArray[i][j] = A[i][j] #Diagonale => Wert bleibt gleich
                else:
                    newArray[i][j] = A[i][j]*-1 #! Diagonale => Wert * -1
            else:
                newArray[i][j] = b.transpose()[i] #Letzter Wert in Array setzt nun den Wert von b ein
    return newArray

def divideByDiagonal(A): #Important: This method is thought to be used after the method addBToA
    newArray = np.zeros((A.shape[0], A.shape[1]))
    diagonale = getDiagonal(A)
    
    for i in range(A.shape[0]):
       for j in range(A.shape[1]):
           if i != j:
               newArray[i][j] = A[i][j]/diagonale[i] 
    return newArray

def getDiagonal(A):
    diagonal = np.zeros((A.shape[0]))
    for i in range(A.shape[0]):
        diagonal[i] = A[i][i]
    return diagonal



def getBFromAB(A):
    indexLastElement = A.shape[1]
    newB = np.zeros((indexLastElement-1))
    for i in range(A.shape[0]):
        newB[i] = A[i][indexLastElement-1]
    return newB

def getAWithoutB(A):
    indexLastElement = A.shape[1]-1
    newA = np.zeros((A.shape[0], indexLastElement))
    for i in range(A.shape[0]):
        for j in range(indexLastElement):
            newA[i][j]= A[i][j]
    return newA

def calcSecondX(A, x, b):
    newX = np.zeros((A.shape[0]))
    for i in range(A.shape[0]):
        zeilVal = 0;
        for j in range(A.shape[1]):
            zeilVal = zeilVal + A[i][j] * x[i] + b[i]
        newX[i] = zeilVal
    return newX


"""
A = np.array([[1,2,3], [2,1,3], [3,1,2]])
b = np.array([2,2,2])

print(A)
print(b.transpose())

addition = addBToA(A, b)
print(addition)
division = divideByDiagonal(addition)
print(division)

b = getBFromAB(division)
calcA = getAWithoutB(division)
print(b)
print(calcA)

loes = calcSecondX(calcA, b, b)
print(loes)


print("----------")
A = np.array([[1,2,3], [2,1,3], [3,1,2]])
b = np.array([2,2,2])

addition = addBToA(A, b)
print(addition)
division = divideByDiagonal(addBToA(A, b))
print(divideByDiagonal(addBToA(A, b)))

b = getBFromAB(division)
calcA = getAWithoutB(division)
print(b)
print(calcA)

loes = calcSecondX(calcA, b, b)
print(loes)
"""