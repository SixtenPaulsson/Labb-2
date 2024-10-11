def powers(list=[], pow1=0, pow2=5):
    power_list = []
    #Loops every number to be exponented
    for num in list:
        #Gör en ny rad som kommer bli inlagd i powerlist
        num_powers = []
        #Loops through the range
        for i in range(pow1,pow2+1):
            #Adds every exponent to num_powers
            num_powers.append(num**i)
        #Adds num_powers to power_list
        power_list.append(num_powers)
    return power_list



def transpose(matrix = []):
    transposed = []
    for height in range(len(matrix)):
        for width in range(len(matrix[0])):
            #Adds another index if needed
            if (len(transposed)==width): transposed.append([])
            #Switches around the numbers
            transposed[width].append(matrix[height][width])
    return transposed


def matmul(matrix1 = [], matrix2 = []):
    new_matrix = []
    matrix2 = transpose(matrix2)
    for m1_rows in range(len(matrix1)):
        new_matrix.append([])
        for m2_coloumns in range(len(matrix2)):
            #Creates a lambda function that multiplies 2 numbers
            #Map loops through the list into the lambda function
            #Summs the result
            summa = sum(map(lambda x,y: x*y , matrix1[m1_rows], matrix2[m2_coloumns]))
            #Appens the summ into the list
            new_matrix[m1_rows].append(summa) 
    return new_matrix

def invert(matrix = [[0,0],[0,0]]):
    #Inverts the function
    #Same code as in the canvas examples
    det = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
    return [[matrix[1][1]/det,-matrix[0][1]/det],
            [-matrix[1][0]/det,matrix[0][0]/det]]

#Loads the text
def loadtxt(filename = ""):
    #Opens the file
    file = open(filename)
    #Reads all the lines
    lines = file.readlines()
    #Loops the lines
    for i in range(len(lines)):
        #Cleans upp the lines
        lines[i]=lines[i].strip("\n").split("\t")
        #Converts both numbers into floats
        lines[i][0] = float(lines[i][0])
        lines[i][1] = float(lines[i][1])
    file.close()
    return lines
