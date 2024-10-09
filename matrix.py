def powers(list=[], pow1=0, pow2=5):
    power_list = []
    #Går igenom varje tal i listan
    for num in list:
        #Gör en ny rad som kommer bli inlagd i powerlist
        num_powers = []
        #Går igenom varje exponent
        for i in range(pow2-pow1+1):
            #Lägger på varje exponent i num_powers
            num_powers.append(num**i+pow1)
        #Lägger till listan i powerlist
        power_list.append(num_powers)
    return power_list

def transpose(matrixes = []):
    transposed = []
    for i in range(len(matrixes)):
        for y in range(len(matrixes[0])):
            #Ifall indexet har slut på platser slängs en ny in
            if (len(transposed)==y): transposed.append([])
            #Slänger in talet i omvända indexet
            transposed[y].append(matrixes[i][y])
    return transposed

#ifall någon läser det här, jag vette fan vad jag gjorde men det här funkar
def matmul(matrix1 = [], matrix2 = []):
    new_matrix = []
    #Transposar andra matrixet, behövs inte men är smidigt
    matrix2 = transpose(matrix2)
    for m1_rows in range(len(matrix1)):
        new_matrix.append([])
        for m2_coloumns in range(len(matrix2)):
            sum = 0
            for m1_coloumns in range(len(matrix1[m1_rows])):
                sum+=matrix1[m1_rows][m1_coloumns]*matrix2[m2_coloumns][m1_coloumns]
            new_matrix[m1_rows].append(sum) 
    return new_matrix

def invert(matrix = [[0,0],[0,0]]):
    #Fett ful kod men det funkar
    det = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
    return [
        [matrix[1][1]/det,-matrix[0][1]/det],
        [-matrix[1][0]/det,matrix[0][0]/det]]
def loadtxt(filename = ""):
    file = open(filename)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip("\n").split("\t")
        lines[i][0] = float(lines[i][0])
        lines[i][1] = float(lines[i][1])
    file.close()
    return lines