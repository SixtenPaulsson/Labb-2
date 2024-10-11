from numpy import *
import matplotlib.pyplot as plt
import sys
def powers(list=[], pow1=0, pow2=5):
    power_list = []
    #Går igenom varje tal i listan
    for num in list:
        #Gör en ny rad som kommer bli inlagd i powerlist
        num_powers = []
        #Går igenom varje exponent
        for i in range(pow1,pow2+1):
            #Lägger på varje exponent i num_powers
            num_powers.append(num**i)
        #Lägger till listan i powerlist
        power_list.append(num_powers)
    return array(power_list)

def poly(a,x):
    Y2 = 0
    for i in range(len(a)):
        Y2 += a[i]*x**i
    return Y2

def main():
    #Loads the file
    data = loadtxt(sys.argv[1]).transpose()
    #Loads the exponent
    n=int(sys.argv[2])
    X=data[0]
    Y=data[1]

    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    X2 = linspace(X[0],X[-1],int(((X[-1]-X[0]))/0.2))
    Y2 = poly(a,X2)

    #Shows the graphs
    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()

if __name__ == "__main__":
    main()