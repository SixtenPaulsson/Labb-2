from matrix import *
import matplotlib.pyplot as plt
import sys

def main():
    #print(sys.argv)

   
    data = loadtxt(sys.argv[1])
    data = transpose(data)
    #print(data)
    X=data[0]
    Y=data[1]
    #print("X = ",X,"Y =",Y)
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)
    #print(Xp,"asd",Yp,"Sak")
    [[b],[m]]  = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    #print(b+m*float(sys.argv[2]))
    #Y2 = map(lambda x: b + m*x,X)
    print(X,Y)
    Y2= []
    for i in X:
        Y2.append(b+m * i)
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    print(Y2)
    plt.show()
    print(Y2)


if __name__ == "__main__":
    main()