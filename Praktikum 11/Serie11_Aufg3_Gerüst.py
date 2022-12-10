# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:43:17 2020

Höhere Mathematik 1, Serie 11, Aufgabe 3 (Gerüst)

@author: knaa
"""
import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(x_min, x_max, y_min, y_max):
    detail = 1000                       #number of pixels in x and y direction
    maxit = 70                          #maximum n for iterations
   
    
    a = np.linspace(x_min, x_max,detail,dtype=np.float64)  #define real axis [x_min,x_max]
    b = np.linspace(y_min, y_max,detail,dtype=np.float64)  #define imaginary axis [y_min,y_max]
    
    B = np.zeros((detail,detail))        #for color values n 
    
    [x,y] = np.meshgrid(a, b)       #to create the complex plane with the axes defined by a and b
    C = x+y*1j                           #creating the plane
    Z = np.zeros(1, np.complex64)  #initial conditions (first iteration), Z has same dimension as C
    for n in np.arange(1,maxit+1):       #start iteration
      Z = Z**2 + C                #calculating Z
      expl = np.where(np.absolute(Z)>2)         #finding exploded values (i.e. with an absolute value > 2)
      Z[expl] = 0                        #removing from iteration
      C[expl] = 0                        #removing from plane
      B[expl] = n                 #saving color value n
    
    B = B/np.max(np.max(B))           #deviding by max value for correct color
    return B, x_min,x_max,y_min,y_max


print("Mandelbrot 1")
B1, x_min1,x_max1,y_min1,y_max1 = mandelbrot(-2.1,0.7,-1.4,1.4)
plt.figure(1)
plt.imshow(B1,extent=[x_min1,x_max1,y_min1,y_max1],origin='lower',interpolation='bilinear')   #display image
print("Mandelbrot 2")
B2, x_min2,x_max2,y_min2,y_max2 = mandelbrot(-0.4,0.1,-1.15,-0.65)
plt.figure(2)
plt.imshow(B2,extent=[x_min2,x_max2,y_min2,y_max2],origin='lower',interpolation='bilinear')   #display image
print("Mandelbrot 3")
B3, x_min3,x_max3,y_min3,y_max3 = mandelbrot(-0.2,-0.1,-1.1,-1.0)
plt.figure(3)
plt.imshow(B3,extent=[x_min3,x_max3,y_min3,y_max3],origin='lower',interpolation='bilinear')   #display image
print("Mandelbrot 4")
B4, x_min4,x_max4,y_min4,y_max4 = mandelbrot(-0.17,-0.15,-1.045,-1.025)
plt.figure(4)
plt.imshow(B4,extent=[x_min4,x_max4,y_min4,y_max4],origin='lower',interpolation='bilinear')   #display image

