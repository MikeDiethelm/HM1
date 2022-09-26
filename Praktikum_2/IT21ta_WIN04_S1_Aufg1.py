# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**5-5*x**4-30*x**3+110*x**2+29*x-105

def ablf(x):
    return 5*x**4-20*x**3-90*x**2+220*x+29

def stammF(x):
    return 

x = np.arange(-10, 11, 0.1)

plt.xlim([-10, 10])
plt.ylim([-1500,1500])

plt.plot(x, f(x))
plt.plot(x, ablf(x))

plt.grid()

plt.show()
    
print("thahte")