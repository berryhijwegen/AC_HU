import numpy as np

ms = np.array([
                [5  ,'x2','x3'],
                ['x4','x5',  4],
                ['x7','x8',  6]
            ])
chars = ['x2','x3','x4','x5','x7','x8']

def generateMagicSquare(ms, chars):
    n = len(ms)
    MAGIC_CONSTANT = n*((n**2+1)/2)

    rowSums = []
    lstV = []

    # This function appends the sum of a full row / column (horizontal/vertical)
    def getSumOfLine(matrix, vertical = False):  
        matrix = np.transpose(matrix) if vertical else matrix

        for i in range(len(matrix)):
            count = MAGIC_CONSTANT
            for element in matrix[i]:
                if element not in chars:
                    count -= int(element)
            rowSums.append(count)

    # This function appends the sum of diagonal line.
    def diagonal(matrix):  
        top = MAGIC_CONSTANT
        for i in range(len(matrix)):
            top -= int(matrix[i][i]) if not matrix[i][i] in chars else 0
        rowSums.append(top)
        rowSums.append(0)

    def getCharPos(matrix, vertical = False):  # to calculate the position of the letters in the vertical and horizontal lines
        matrix = np.transpose(matrix) if vertical else matrix

        for i in range(len(matrix)):
            temp = [0, 0, 0, 0, 0, 0]
            for j in range(len(matrix[i])):
                if matrix[i][j] in chars:
                    index = chars.index(matrix[i][j])
                    temp[index] = 1
            lstV.append(temp)


    # This function calculates the position of the characters in the diagonal line from top-left to bottom-right.
    def getDiagonalCharPos(matrix):
        for i in range(len(matrix)):
            temp = [0, 0, 0, 0, 0, 0]
            if matrix[i][i] in chars:
                index = chars.index(matrix[i][i])
                temp[index] = 1
                lstV.append(temp)
        lstV.append(temp)


    getSumOfLine(ms)
    getSumOfLine(ms, vertical=True)
    diagonal(ms)
    getCharPos(ms)
    getCharPos(ms, vertical=True)
    getDiagonalCharPos(ms)

    unknownVars = np.linalg.pinv(np.array(lstV)).dot(np.array(rowSums))

    count = 0
    for row in range(len(ms)):
        for column in range(len(ms[row])):
            if(not ms[row][column].isdigit()):
                ms[row][column] = unknownVars[count]
                count+=1
    return ms.astype(np.float)

print("Magic Square:")
print(generateMagicSquare(ms, chars))