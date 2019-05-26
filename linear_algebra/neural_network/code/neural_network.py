import sys, json, numpy as np
from functions import calculateOutput, generateMatrixFromJson

# stop if argument is not given
if len(sys.argv) < 2:
    sys.exit("Add JSON-file name!")

with open(sys.argv[1]) as json_file:  
    data = json.load(json_file)
    
    inputVector = np.ones(data['layer1']['size_in'])
    layers = list(data.values())
    output = None
    for i in range(len(layers)):
        matrixLayer = generateMatrixFromJson(layers[i])
        functionInput = inputVector if i == 0 else output
        output = calculateOutput(functionInput, matrixLayer, layers[i]['size_out'])
    print("Output:")
    print(output)