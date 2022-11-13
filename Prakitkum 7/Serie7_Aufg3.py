import numpy as np
import matplotlib.pyplot as plt

def findXVector(A,b):
    round = 0
    while round < A.shape[0]:
        #if(A[round][round] != 0):
        b[round][0] = b[round][0] / A[round][round]
        round +=1
    return b

def jordan(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = x_dim-1
    while round >= 0:
        nextLine = round-1
        while nextLine >= 0:
            #if(A[round][round]!= 0 ):
            divideBy = A[nextLine][round] / A[round][round]
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            for item in range(y_dim):
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
            nextLine = nextLine -1
        round = round -1
    #print("result Jordan: ")
    #print(A)
    #print(b)
    return findXVector(A, b)

def gaus(A, b):
    x_dim = A.shape[0]
    y_dim = A.shape[1]
    round = 0
    while round <= x_dim:
        nextLine = round +1
        while nextLine <= x_dim-1:
            #if(A[round][round]!= 0 ):
            divideBy = A[nextLine][round] / A[round][round]
            b[nextLine][0] = b[nextLine][0] - divideBy * b[round][0]
            
            for item in range(y_dim):
                A[nextLine][item] = A[nextLine][item] - divideBy * A[round][item]
            nextLine = nextLine +1
        round = round +1
    
    #print("Result Gauss: ")
    #print(A)
    #print(b)
    return jordan(A, b)
 
def polynom(c, arr): 
    return arr[0][0]*c**3+arr[0][1]*c**2+arr[0][2]*c+arr[0][3]
    
def showPlot(x):
    a = np.arange(-5.0, 20.0, 0.5)
    print('Wenn man x = 2')
    print(np.polyval(x, 2))
    print(2, x.transpose())
    plt.plot(polynom(a, x.transpose()))
    #plt.plot(np.transpose(x), a)
    
def startMethod():
    Matrix_A = np.array([[13,1,1,1],[1,9,1,1], [1,1,2,1],[0,0,0,1]])
    Vector_b = np.array([[152, 172, 104,150]])
    Vector_b = np.transpose(Vector_b)
    print("Start matrix: ")
    print(Matrix_A)
    print("start B: ")
    print(Vector_b)
    foundX = gaus(Matrix_A, Vector_b)
    print(foundX)
    showPlot(foundX)
    print("Calculated x Vector:")
    print(foundX)

#Aufgabe 2 (startMethod):
startMethod()