import numpy as np
import itertools
import matplotlib.pyplot as plt

class Flumph:
    def __init__(self, states, chances, startChances):
        self.states = states
        self.chances = chances
        self.startChances = startChances

    def generateChances(self):
        currVector = self.startChances
        data = {}
        for i in range(len(self.states)):
            data[i] = []
        
        count = 0
        while(True):
            prevcV = currVector
            print(currVector)
            currVector = np.dot(currVector, self.chances)
            for i in range(len(currVector)):
                data[i].append(currVector[i])
            count+=1
            for i in range(len(currVector)):
                if(currVector[i] > 0.99):
                    return self.states, data
            if(np.array_equal(prevcV,currVector)):
                return self.states, data 

    def plotChances(self):
        toestanden, data = self.generateChances()

        x = list(range(len(data[0])))
        for i in range(len(data)):
            plt.plot(x, data[i])

        plt.gca().legend(toestanden.values())
        plt.ylabel('Kans')
        plt.xlabel('Dagen')
        plt.show()

    def getTensorProduct(self, steps = 1):
        value = self.startChances
        for i in range(steps):
            value = np.outer(self.chances, value)
        return value