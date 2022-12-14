# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:10:15 2022

@author: Benssy
"""

import numpy as np
from matplotlib import pyplot as plt


plt.figure(1)
def f1(x):
    return x**7-14*x**6+84*x**5-280*x**4+560*x**3-672*x**2+448*x-128
x = np.linspace(1.99, 2.01, 501)
plt.plot(x, f1(x))
plt.title("2a, f1")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.grid()
plt.show()
#Antwort zu 2a zu der Funktion f1:
#Nicht die entsprechende Funktion da es mehrere Potenzen gibt und somit höhere Potenzen grösseren Wert haben.
#Kleinere Potenzen werden abgerundet und somit entstehen immer grössere Rundungsfehler.
#Die Maschinengenauigkeit spielt daher eine grosse Rolle. 


plt.figure(2)
def f2(x):
    return (x-2)**7
x = np.linspace(1.99, 2.01,501)

plt.plot(x, f2(x))
plt.title("2a, f2")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.grid()
plt.show()
#Antwort zu 2a zu der Funktion f2:
#Stellt die gewohnte Funktion dar, da es nur eine Potenz gibt. Die Maschinengenauigkeit spielt daher keine Rolle. 


plt.figure(3)
schrittweite = pow(10, -17)
min = -pow(10, -14)
max = +pow(10, -14)
x = np.arange(min, max, schrittweite)
def f3(x):
    return x / (np.sin(1 + x) - np.sin(1))
plt.title("2b")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.plot(x, f3(x))
plt.grid()
plt.show()
#Antwort zu 2b zu der Funktion f3:
#Nein, ist nicht stabil. Die relativen Fehler werden immer grösser. Der Graph ist nicht gleich der Funktion dargestellt.


plt.figure(4)
schrittweite = pow(10, -17)
min = -pow(10, -14)
max = +pow(10, -14)
x = np.arange(min, max, schrittweite)
def f4(x):
    return x / (2 * np.cos((1 + x + 1) / 2) * np.sin((1 + x - 1) / 2))
plt.title("2c")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.plot(x, f4(x))
plt.grid()
plt.show()
#Antwort zu 2c zu der Funktion f4:
#Grenzwert beträgt genau 0. Graph entspricht der Funktion, da es weniger Additionen und Subtraktionen hat.