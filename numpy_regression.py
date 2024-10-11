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
    print("x",x,type(x))

    #print("a",a)
    for i in range(len(a)):
        #print("AI grejen",a[i]*i)
        Y2 += a[i]*x**i
    #print(Y2)
    return Y2

def main():
    #print(sys.argv)
    data = loadtxt(sys.argv[1])
    n=int(sys.argv[2])
    data=data.transpose()
    X=data[0]
    Y=data[1]
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    plt.plot(X,Y,'ro')
    print(((X[-1]-X[0]))/0.2)
    steps = int(((X[-1]-X[0]))/0.2)
    X2 = linspace(X[0],X[-1],steps)
    print(X2)
    Y2= poly(a,X2)
    plt.plot(X2,Y2)
    print(X2,Y2)
    plt.show()

if __name__ == "__main__":
    main()