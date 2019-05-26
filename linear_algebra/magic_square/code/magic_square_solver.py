# Function to print the original matrix  
def printFilledDiagonal(sq):  
    n = len(sq)
    MAGIC_CONSTANT = int(n*((n**2+1)/2))
    def generateMagicSquare(sq):
        # Get magic constant
        for i in range(0, 9):  
            rowSum = 0
            for j in range(0, 3):  
                rowSum += sq[i][j]
            sq[i][i] = MAGIC_CONSTANT - rowSum  
        for i in range(0, 3):  
            for j in range(0, 3):  
                print(sq[i][j], end = " ")  
            print() 

    def isMagicSquare(sq):
        n = len(sq)
        for i in range(0, n):
            rowSum = 0
            for j in range (0, n):
                rowSum += sq[i][j]
                if(sq[i][j] == 0):
                    return False
            if(rowSum != MAGIC_CONSTANT):
                return False
        return True
    generateMagicSquare(sq)
            
sq = [
        [0, 0, 0],  
        [9, 0, 0],  
        [4, 3, 0]
    ]  
printFilledDiagonal(sq)