"""
Praktikum 9: 26.11.2022

Author:Adrian Moser, Mike Diethelm, Benssy Kolattukudy
"""
from math import nan
import numpy as np


def berechneX(A, b):
    return np.linalg.solve(A, b)

def getCond(M):
    return np.linalg.cond(M, np.inf)

def conditionalBruch(A, Agestoert):
    return (getNorm2(Agestoert,A)/getNorm(A))

def getNorm(c):
    return np.linalg.norm(c, np.inf)

def getNorm2(cGestört,cNormal):
    return np.linalg.norm(cGestört-cNormal, np.inf)

def normBruch(b, bGestoert):
    return (getNorm2(bGestoert,b)/getNorm(b))

def leftMultiplication(A, Agestoert):
    return getCond(A) / (1- (getCond(A) * conditionalBruch(A, Agestoert)))

def rightMultiplication(A, Agestoert, b, bGestoert):
    return conditionalBruch(A, Agestoert) + conditionalBruch(b, bGestoert)

def berechneDxMax(A, Agestoert, b, bGestoert):
    if(getCond(A) * conditionalBruch(A, Agestoert) == 1):
        print("Is nan")
        return float('nan')
    else:
        return leftMultiplication(A, Agestoert) * rightMultiplication(A, Agestoert, b, bGestoert)

def berechneDxObs(x, xGestoert):
    return (getNorm2(xGestoert,x)/getNorm(x))

#Aufgabe 2:
# Definiere die Matrix A und den Vektor b, sowie die gestörte Matrix A und der gestörte Vektor b.

A = np.array([[1,0,2], [0,1,0], [10**-4, 0, 10**-4]])

Agestoert = A + 10**-7

b = np.array([1,1,0])

bGestoert = np.array([1,1, 1.667*10**-7])

# Aufgabenstellung printen 

print("Die Matrix A und deren gestörte Matrix Agestoert:")
print(A)
print(Agestoert)

print("Die Vektoren b und bGestoert: ")

print(b)
print(bGestoert)

print("Berechneter x Wert")

x = berechneX(A, b)
xGestoert = berechneX(A, bGestoert)

print('x',x)
print("und der berechnete gestörte X Wert")
print(xGestoert)

print("Zuletzt noch dMax:")

d = berechneDxMax(A, Agestoert, b,bGestoert)

if(d == nan):
    print("Leiter sind die Zahlen nicht zum rechnen geeignet")
else:
    print(d)

print("und der relative Fehler x")
print(berechneDxObs(x,xGestoert))


