# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:48:22 2022

@author: Adrian Moser
"""
import matplotlib.pyplot as plt
import numpy as np


"----------------------------------------------------------------------"
"-------------------------------- Aufgabe a ---------------------------"
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

def runAufgabeA():
    x = 6
    resultetXValues = np.array([])
    resultetYValues = np.array([])
    calculatedResult = 0

    while x <= 2000:
        calculatedResult = calculateCircumfence(x)
        resultetXValues = np.append(resultetXValues, x)
        resultetYValues = np.append(resultetYValues, calculatedResult)
        x = x*2
     
    plt.plot(resultetXValues, resultetYValues)  
    #plt.ylabel("Umfang")
    #plt.xlabel("Anzahl Ecken")
    #plt.legend(["Aufgabe 3 a"])
    #plt.grid() 
    #plt.show() #show wird weiter unten gestarted

antwortA = "Wie man sieht entsteht eine Funktion die sich an 2 * PI nähert, sieh aber nie erreicht, da Python keine irrationalen Zahlen zeigen kann sondern nur eine MaschinienZahl"

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
        return 1.0
    else:
        return np.sqrt(overBruch(x) / underBruch(x))

def runAufgabeB():
    startX = 6
    resultetXValues2 = np.array([])
    resultetYValues2 = np.array([])
    calculatedResult2 = 0
    
    while startX <= 2000:
        calculatedResult2 = startX * bOuterRoot(startX)
        resultetXValues2 = np.append(resultetXValues2, startX)
        resultetYValues2 = np.append(resultetYValues2, calculatedResult2)
        startX = startX*2
    
     
    
    plt.plot(resultetXValues2, resultetYValues2)
    #plt.ylabel("Umfang")
    #plt.xlabel("Anzahl Ecken")
    #plt.legend(["Aufgabe 3 b"])
    #plt.grid()
    #plt.show()

antwortB = "Da die beiden Funktionen aufeinander liegen, bedeutet diese dass die Funktion die gleiche Werte erhält für die Anzahl Ecken und dabei auch nicht 2 * PI erreichen, da dies keine MaschinenZahl ist."

"----------------------------------------------------------------------"
"-------------------------------- Starter of a + b ---------------------------"

runAufgabeA()
runAufgabeB()

plt.ylabel("Umfang")
plt.xlabel("Anzahl Ecken")
plt.legend(["Aufgabe 3 a", "Aufgabe 3 b"])
plt.grid()
plt.show()
print(antwortA)
print()
print(antwortB)