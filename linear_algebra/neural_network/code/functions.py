import numpy as np

# This function generates a matrix from the given JSON file.
# Missing values are random generated and placed into the matrix.
def generateMatrixFromJson(json):
    currentLayer = json
    weightMatrix = np.zeros((currentLayer['size_out'], currentLayer['size_in']))
    
    weights = currentLayer['weights']
    for node in weights:
        for i in range(1, currentLayer['size_out'] + 1):
            try:
                weights[node][str(i)]
            except KeyError:
                weights[node][str(i)] = 0
            weightMatrix[i - 1][int(node) - 1] = weights[node][str(i)] 
    return weightMatrix

# This function does matrix-vector multiplication.
# It takes the first row of the matrix and multiplicates all the values in that row with the first value in the vector,
# this process is the same for every row.
def calculateOutput(inputVector, weights, outputSize):
    output = np.zeros((outputSize, np.size(inputVector, 1)))
    for k in range(0, np.size(inputVector, 1)):
        for i in range(0, len(weights)):
            for j in range(0, len(weights[i])):
                print(i,j,k)
                output[i][k] += inputVector[j][k] * weights[i][j]
    return output

def numeric(d):
    for k, v in d.items():
        if isinstance(v, dict):
            numeric(v)
        else:
            try:
                if(k != 'size_in' and k != 'size_out'):
                    d[k] = float(v)
                else:
                    d[k] = int(v)
            except:
                pass
    return d