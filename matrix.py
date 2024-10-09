def powers(list=[], pow1=0, pow2=5):
    power_list = []
    for num in list:
        num_powers = []
        for i in range(pow2-pow1+1):
            num_powers.append(num**i+pow1)
        power_list.append(num_powers)
    return power_list

def transpose(matrixes = []):
    transposed = []
    for i in range(len(matrixes)):
        for y in range(len(matrixes[0])):
            #Lite av en fullösning här, ska fixa
            if len(transposed)==y: transposed.append([])
            transposed[y].append(matrixes[i][y])
    #print(transposed)
    return transposed

#def matmul(matrix1 = [], matrix2 = []):
#    pass
#def invert(matrix = []):
#    pass
#def loadtxt(filename = ""):
#    file = open(filename)
#    print(file.read)
#    file.close()
#    pass

powers([1,2,3],3,5)