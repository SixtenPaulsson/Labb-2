from matrix import *
import matplotlib.pyplot as plt
import sys

def main():
    #Loads the file
    data = transpose(loadtxt(sys.argv[1]))
    X=data[0]
    Y=data[1]

    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]]  = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    #Converts the Y2 values
    Y2=list(map(lambda x: b+ m*x, X))

    #Shows the graphs
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()


if __name__ == "__main__":
    main()