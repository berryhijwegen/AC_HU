import sys, json, numpy as np
from functions import calculateOutput, generateMatrixFromJson

# stop if argument is not given
if len(sys.argv) < 2:
    sys.exit("Add JSON-file name!")

# Load the file with the file name given in argument
with open(sys.argv[1]) as json_file:  
    data = json.load(json_file)
    
    inputVector = np.ones(data['layer1']['size_in'])
    layers = list(data.values())
    output = None
    for i in range(len(layers)):
        # For each layer the algorithm creates a matrix with weights from the JSON file. 
        # For the first row it takes a vector of all ones. Every layer after that it uses the output from the layer before it.
        matrixLayer = generateMatrixFromJson(layers[i])
        functionInput = inputVector if i == 0 else output
        print(matrixLayer)
        print(functionInput)
        print()
        output = calculateOutput(functionInput, matrixLayer, layers[i]['size_out'])
    print("Output:")
    print(output)