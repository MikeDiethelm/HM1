# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:43:17 2020

Höhere Mathematik 1, Serie 11, Aufgabe 3 (Gerüst)

@author: knaa
"""
import numpy as np
import matplotlib.pyplot as plt


detail = 1000                       #number of pixels in x and y direction
maxit = 70                          #maximum n for iterations
x_min = """???"""                   #minimim value of x-interval
x_max = """???"""                   #maximum value of x-interval
y_min = """???"""                   #minimim vale of y-interval
y_max ="""???"""                    #minimim vale of y-interval

a = np.linspace("""???""",detail,dtype=np.float64)  #define real axis [x_min,x_max]
b = np.linspace("""???""",detail,dtype=np.float64)  #define imaginary axis [y_min,y_max]

B = np.zeros((detail,detail))        #for color valzues n 

[x,y] = np.meshgrid("""???""")       #to create the complex plane with the axes defined by a and b
C = x+y*1j                           #creating the plane
Z = np.zeros("""???""", np.complex64)  #initial conditions (first iteration), Z has same dimension as C
for n in np.arange(1,maxit+1):       #start iteration
  Z = """???"""                      #calculating Z
  expl = np.where("""???""")         #finding exploded values (i.e. with an absolute value > 2)
  Z[expl] = 0                        #removing from iteration
  C[expl] = 0                        #removing from plane
  B[expl] = """???"""                #saving color value n

plt.figure(1)
B = B/np.max(np.max(B))           #deviding by max value for correct color
plt.imshow(B,extent=[x_min,x_max,y_min,y_max],origin='lower',interpolation='bilinear')   #display image


