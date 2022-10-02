# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:09:26 2022

@author: Mike Diethelm
"""
import numpy as np
from matplotlib import pyplot as plt

  
def upAndDownDerivate(a, xmin, xmax):
    
    #KoeffizientenVektor
    a = np.array(a)
    x = np.linspace(xmin, xmax, 100)
    f = np.zeros(len(x))
    downF = np.zeros(len(x))
    upF = np.zeros(len(x))

    for n in range(len(a)):
        f += a[n] * x ** n
        downF += n * a[n] * x**(n-1)
        upF += (1/(n+1)) * a[n] * x**(n+1)

    return (x, f, downF, upF)


x, f, fDown, fUp = upAndDownDerivate([-105, 29, 110, -30, -5, 1], -10, 10)

plt.plot(x, f)
plt.plot(x, fDown)
plt.plot(x, fUp)
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.title("Funktionen und ihre Ableitungen / Stammfunktionen")
plt.legend(["Function", "Ableitung", "Stammfunktion"])
plt.grid(color='lightgray', linestyle='-', linewidth=1)

plt.xlim(right=10)
plt.xlim(left=-8)
plt.ylim(top=1500)
plt.ylim(bottom=-1500)

plt.show()
