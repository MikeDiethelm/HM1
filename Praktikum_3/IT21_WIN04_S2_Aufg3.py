# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:48:22 2022

@author: adria
"""
import matplotlib.pyplot as plt
import numpy as np

def bruch(x):
    return (outerRoot(x/2) ** 2) / 4

def innerRoot(x):
    return 2*np.sqrt(1-bruch(x))

def outerRoot(x):
    if(x == 6):
        return 1
    else:
        return np.sqrt(2 - innerRoot(x))

def calculateCircumfence(x):
    return x * outerRoot(x)


x = 6
resultetXValues = np.array([])
resultetYValues = np.array([])
calculatedResult = 0
while x <= 500:
    calculatedResult = calculateCircumfence(x)
    resultetXValues = np.append(resultetXValues, x)
    resultetYValues = np.append(resultetYValues, calculatedResult)
    x = x*2
    
#plt.plot(resultetXValues, resultetYValues)
#plt.ylabel("Umfang")
#plt.xlabel("Anzahl Ecken")
#plt.show()
#print("Je grösser die Anzahl Ecken, desto näher an 2*Pi kommen wir.")


"----------------------------------------------------------------------"
"-------------------------------- Aufgabe b ---------------------------"

def innerRoot2(x):
    return np.sqrt(1 - (bOuterRoot(x/2) **2 / 4))


def overBruch(x):
    return bOuterRoot(x/2) ** 2

def underBruch(x):
    return 2* (1 + innerRoot2(x))
    
def bOuterRoot(x):
    if(x == 6):
        return 1
    else:
        return np.sqrt(overBruch(x) / underBruch(x))

startX = 6
resultetXValues2 = np.array([])
resultetYValues2 = np.array([])
calculatedResult2 = 0

while startX <= 500:
    calculatedResult2 = startX * bOuterRoot(startX)
    resultetXValues2 = np.append(resultetXValues2, startX)
    resultetYValues2 = np.append(resultetYValues2, calculatedResult2)
    startX = startX*2

    
plt.plot(resultetXValues, resultetYValues)    
plt.plot(resultetXValues2, resultetYValues2)
plt.ylabel("Umfang")
plt.xlabel("Anzahl Ecken")
plt.legend(["Aufgabe 3 a", "Aufgabe 3 b"])
plt.show()
#print("Je grösser die Anzahl Ecken, desto näher an 2*Pi kommen wir.")