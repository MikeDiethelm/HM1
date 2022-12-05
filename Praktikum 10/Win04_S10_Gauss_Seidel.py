# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:05:15 2022

@author: adria
"""
import numpy as np

def gaussSeidelVerfahren(A, b, x0, tol):
    L = np.tril(A,k=-1)
    D = np.diag(np.diag(A))
    R = np.triu(A, k=1)
    return "not done"

def getLDInvert(A):
    L = np.tril(A,k=-1)
    D = np.diag(np.diag(A))
    #LD = L+D
    print(L)
    print(D)
    return np.linalg.inv(D+L)


A = [[2,3,4],[4,5,6], [7,8,9]]
print(A)
print(getLDInvert(A))