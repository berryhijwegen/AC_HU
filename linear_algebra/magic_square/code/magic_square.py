import numpy as np

# Works with 3x3 and 4x4
# Insert np array at variable matrix
matrix = np.array([
                [13 ,'x2','x3', 12],
                [2  ,'x6','x7',  7],
                ['x9','x10', 4,'x12'],
                ['x13','x14',15,1]
            ])

# Append all unknown in one list
chars = []
for row in matrix:
    for element in row:
        if 'x' in element:
            chars.append(element)

def generateMagicSquare(matrix, chars):
    n = len(matrix)
    MAGIC_CONSTANT = n*((n**2+1)/2)

    rowSums = []
    charPositions = []

    # This function appends the sum of a full row / column (horizontal/vertical)
    def appendSumOfLine(matrix, vertical):  
        matrix = np.transpose(matrix) if vertical else matrix

        for i in range(len(matrix)):
            count = MAGIC_CONSTANT
            for element in matrix[i]:
                if element not in chars:
                    count -= int(element)
            rowSums.append(count)

    # This function appends the sum of diagonal line.
    def appendDiagonalSum(matrix):  
        top = MAGIC_CONSTANT
        for i in range(len(matrix)):
            top -= int(matrix[i][i]) if not matrix[i][i] in chars else 0
        rowSums.append(top)
        rowSums.append(0)

    # This function generates the position of the characters in the horizontal and vertical axis,
    # appends them after.
    def appendCharPos(matrix, vertical):  
        matrix = np.transpose(matrix) if vertical else matrix

        for i in range(len(matrix)):
            temp = [0] * len(chars)
            for j in range(len(matrix[i])):
                if matrix[i][j] in chars:
                    index = chars.index(matrix[i][j])
                    temp[index] = 1
            charPositions.append(temp)


    # This function generates the position of the characters in the diagonal line from top-left to bottom-right,
    # appends them after.
    def appendDiagonalCharPos(matrix):
        for i in range(len(matrix)):
            temp = [0] * len(chars)
            if matrix[i][i] in chars:
                index = chars.index(matrix[i][i])
                temp[index] = 1
                charPositions.append(temp)
        charPositions.append(temp)


    appendSumOfLine(matrix, False)
    appendSumOfLine(matrix, True)
    appendDiagonalSum(matrix)
    appendCharPos(matrix, False)
    appendCharPos(matrix, True)
    appendDiagonalCharPos(matrix)

    unknownVars = np.linalg.pinv(np.array(charPositions)).dot(np.array(rowSums))

    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if(not matrix[row][column].isdigit()):
                matrix[row][column] = unknownVars[count]
                count+=1

    return matrix.astype(np.float)

print("Magic Square:")
print(generateMagicSquare(matrix, chars))