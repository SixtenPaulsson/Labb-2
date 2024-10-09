#def powers(list, num1, num2):
#    pass
def transpose(matrixes = []):
    transposed = []
    for i in range(len(matrixes)):
        for y in range(len(matrixes[0])):
            #Lite av en fullösning här, ska fixa
            if len(transposed)==y: transposed.append([])
            transposed[y].append(matrixes[i][y])
    print(transposed)
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