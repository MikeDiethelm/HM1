# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:13:48 2022 

@author: Adrian, Benssy, Mike
"""
import numpy as np

def berechneZeichen(A):
    L = np.tril(A, k=-1)
    D = np.diag(np.diag(A))
    R = np.triu(A, k=1)
    n = 1 #Zählt die Anzahl der Berechnungen
    return L, D, R, n

def berechneAPriori(A, x, xn, tol):
    
    bruchunten = np.linalg.norm((xn-x),np.inf)*(1 - np.linalg.norm(A,np.inf))
    gesamtbruch= tol / bruchunten
    
    grossBruchoben = np.log(gesamtbruch)
    
    grossBruchunten = np.log(np.linalg.norm(A, np.inf))
    return grossBruchoben / grossBruchunten

def berechneAPosteriori(A, xn, xn_minuseins):
    bruchoben = np.linalg.norm(A, np.inf)
    bruchunten = 1 - np.linalg.norm(A,np.inf)
    rechtseitig = np.linalg.norm(xn - xn_minuseins)
    
    return (bruchoben / bruchunten) * rechtseitig

def jacobiIteration(A, c, xn):
    return A@xn+c

def gaussSeidelIteration(A, c, xn):
    return  A @ xn + c
    
def startPoint(A, b, x0, tol, opt):
    
    optionBekannt = True
    L, D, R, n = berechneZeichen(A)
    
    if(opt == "J"):
        B = -np.linalg.inv(D) @ (L+R)
        c = np.linalg.inv(D) @ b
        ersteIteration = jacobiIteration(B, c, x0)
    elif(opt == "GS"):
        B = -np.linalg.inv(D+L) @ R
        c =  np.linalg.inv(D+L) @ b
        ersteIteration = gaussSeidelIteration(B, c, x0)
    else:
        print("Option nicht bekannt") 
        print(opt)
        optionBekannt = False
        
    xn = np.copy(ersteIteration)
    xn_minuseins = np.copy(x0)
    
    #Berechne A-priori
    n2 = berechneAPriori(B, x0, ersteIteration, tol)
    
    #nun wird der Wert tol auch beachtet
    while tol < berechneAPosteriori(B, xn, xn_minuseins) and optionBekannt:
        xn_minuseins = np.copy(xn)
        
        if(opt == "J"):
            #B = -np.linalg.inv(D) @ (L+R) wird nicht mehr geändert
            #c = np.linalg.inv(D) @ b
            xn = jacobiIteration(B, c, xn)
        else:
            #B = -np.linalg.inv(D+L) @ R
            #c =  np.linalg.inv(D+L) @ b
            xn = gaussSeidelIteration(B, c, xn)
        n += 1
    
    return (xn, n, n2)
