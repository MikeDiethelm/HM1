import numpy as np
import matplotlib.pyplot as plt

def findXVector(A,b):
    round = 0
    while round < A.shape[0]:
        #if(A[round][round] != 0):
        divideBy = 1
        if(A[round][round]!=0):
            divideBy = A[round][round]
        b[round][0] = b[round][0] / divideBy
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
            divideBy = 1
            if(A[round][round]!=0):
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
            print(A[nextLine][round])
            print(A[round][round])
            divideBy = 1
            if(A[round][round]!=0):
                divideBy = A[nextLine][round] / A[round][round]
            print(b[nextLine][0])
            print(divideBy)
            print(b[round][0])
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
    return arr[0][0]*c**3+arr[0][1]*c**2+arr[0][2]*c+150
    
def showPlot(x):
    a = np.arange(0, 15.0, 1)
    print('Wenn man x = 2')
    print(np.polyval(x,2))
    print(polynom(2, x))
    
    plt.xlim(-5, 15)
    plt.plot(a, x)
    print('polyfit')
    print(np.polyval(x, 3))
    #plt.plot(np.transpose(x), a)
    
def startMethod():
    Matrix_A = np.array([[0,0,0,1], [2**3,2**2,2,1], [9**3,9**2,9,1], [13**3,13**2,13, 1]])
    Vector_b = np.array([[150, 104, 172, 152]])
    Vector_b = np.transpose(Vector_b)
    print("Start matrix: ")
    print(Matrix_A)
    print("start B: ")
    print(Vector_b)
    #foundX = gaus(Matrix_A, Vector_b)
    #print(foundX)
    y = np.linalg.solve(Matrix_A, Vector_b)
    print(y)
    showPlot(y.transpose())
    print("Calculated x Vector:")
    print(y)
    
    

#Aufgabe 2 (startMethod):
startMethod()