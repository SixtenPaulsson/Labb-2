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

def matmul(matrix1 = [], matrix2 = []):
    new_matrix = []
    #Behövs egentligen inte men är smidigt
    matrix2 = transpose(matrix2)
    for x in range(len(matrix1)):
        new_matrix.append([])
        for y in range(len(matrix2)):
            sum = 0
            for a in range(len(matrix1[x])):
                sum+=matrix1[x][a]*matrix2[y][a]
            new_matrix[x].append(sum) 
    return new_matrix

#def invert(matrix = []):
#    pass
#def loadtxt(filename = ""):
#    file = open(filename)
#    print(file.read)
#    file.close()
#    pass



matmul([[0,1]
     ,[1,0]
     ],[[1, 0]
     ,[0,-1]
     ])