
from math import nan
import numpy as np
import matplotlib.pyplot as plt

def berechneX(A, b):
    return np.linalg.solve(A, b)

def getCond(M):
    return np.linalg.norm(M, np.inf)

def conditionalBruch(A, Agestoert):
    return (getCond(A)-getCond(Agestoert))/getCond(A)

def getNorm(c):
    return np.linalg.norm(c, np.inf)

def normBruch(b, bGestoert):
    return (getNorm(b)-getNorm(bGestoert))/getNorm(b)

def leftMultiplication(A, Agestoert):
    return getCond(A) / (1- (getCond(Agestoert) * conditionalBruch(A, Agestoert)))

def rightMultiplication(A, Agestoert, b, bGestoert):
    return conditionalBruch(A, Agestoert) + normBruch(b, bGestoert)

def berechneDxMax(A, Agestoert, b, bGestoert):
    if(getCond(A) * conditionalBruch(A, Agestoert) < 1):
        return float('nan')
    else:
        return leftMultiplication(A, Agestoert) * rightMultiplication(A, Agestoert, b, bGestoert)

def berechneDxObs(x, xGestoert):
    return (getNorm(x)-getNorm(xGestoert))/getNorm(x)

#Aufgabe 2:
# Definiere die Matrix A und den Vektor b, sowie die gestörte Matrix A und der gestörte Vektor b.

A = np.array([[1,0,2], [0,1,0], [10**-4, 0, 10**-4]])

Agestoert = A + 10**-7

b = np.array([1,1,0])

bGestoert = np.array([1,1, 168325*10**-11])

max = np.zeros(1000)
dObsA = np.zeros(1000)
for i in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)
    A_tilde = A + np.random.rand(100, 100)/10**5
    b_tilde = b + np.random.rand(100, 1)/10**5
    dMax = berechneDxMax(A,A_tilde,b,b_tilde)
    dObs = berechneDxObs(berechneX(A,b),berechneX(A_tilde,b_tilde))
 
    max[i] = dMax
    dObsA[i] = dObs

factor = max/dObsA

# generate and center the axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# plot the functions
plt.title("Excercise 9\n\n")
plt.grid()
plt.plot(dObsA, max, '.b', label="factor = dx_max/dx_obs")
plt.semilogy()
plt.legend()
plt.show(block=False)


factor = sorted(factor)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# plot the functions
plt.title("Excercise 9\n\n")
plt.grid()
plt.plot(factor, '.r', label="factor distribution")
plt.ylim([-10**(5), 10**5])
#plt.semilogy()
plt.legend()
plt.show()