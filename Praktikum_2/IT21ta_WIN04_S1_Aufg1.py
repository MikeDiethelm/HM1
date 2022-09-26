# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**5-5*x**4-30*x**3+110*x**2+29*x-105

#def plotting():
    #plt.xlim()
    #plt.ylim()

x = np.arange(-10, 11, 1)

plt.xlim()
plt.ylim()

plt.plot(x, f(x))

plt.grid()

plt.show()
    
print("thahte")