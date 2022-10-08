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
    
plt.plot(resultetXValues, resultetYValues)
plt.ylabel("Umfang")
plt.xlabel("Anzahl Ecken")
plt.show()
print("Je grösser die Anzahl Ecken, desto näher an 2*Pi kommen wir.")


"----------------------------------------------------------------------"
"-------------------------------- Aufgabe b ---------------------------"



