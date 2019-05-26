import numpy as np

def generateMatrixFromJson(json):
    currentLayer = json
    weightMatrix = np.zeros((currentLayer['size_out'], currentLayer['size_in']))
    
    weights = currentLayer['weights']
    for node in weights:
        for i in range(1, currentLayer['size_out'] + 1):
            try:
                weights[node][str(i)]
            except KeyError:
                randonNumber = round(np.random.uniform(-1.0,1.0), 1) 
                weights[node][str(i)] = randonNumber
            weightMatrix[i - 1][int(node) - 1] = weights[node][str(i)] 
    return weightMatrix

def calculateOutput(inputVector, weights, outputSize):
    output = np.zeros((outputSize, 1))
    for i in range(0, len(weights)):
        for j in range(0, len(weights[i])):
            output[i] += inputVector[j] * weights[i][j]
    return output