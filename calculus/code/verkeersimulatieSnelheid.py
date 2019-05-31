import functions
import csv
import matplotlib.pyplot as plt

directions = functions.getDirections('resources/verkeerssimulatie-richting.csv')

carPositions    = {
        1: [0,0],
        2: [0,0],
        3: [0,0]
    }
currentSpeed    = [0.0,0.0,0.0]
carColor        = ['red','blue','green']
plt.axhline(0, color='black', linewidth=25, zorder=1)
plt.axvline(0, color='black', linewidth=25, zorder=1)

with open('resources/verkeerssimulatie-rechteweg-snelheden.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    prevRow = None

    for row in csv_reader:
        # Get positions from first row
        if(line_count == 0):
            
            positions = row[1:]
            for i in range(len(positions)):
                carPositions[i + 1] = [0, int(positions[i])] if directions[i + 1] == 'v' else [int(positions[i]), 0]

        # For all other rows (speeds)        
        else:
            timestamp = row[0]

            # For each car get the direction and get new position,
            # calculated by position = old position + speed * Δtime (Constant 0.1)
            for i in range(len(row[1:])):

                currentSpeed[i] = float(row[i+1])
                index = 1 if directions[i + 1] == 'v' else 0
                carPositions[i + 1][index] += currentSpeed[i] * 0.1

                plt.scatter(carPositions[i + 1][0],carPositions[i + 1][1], color=carColor[i], s=15, zorder=10) 
                plt.pause(0.1)

            # Check if 2 cars bumped in to each other
            for carPos1 in carPositions:

                # Get length of car in right direction    
                distanceCoordinates1 = [2,1.5] if directions[carPos1]  == 'h' else [1.5,2]
                for carPos2 in carPositions:

                    if(abs(carPositions[carPos1][0]-carPositions[carPos2][0]) < distanceCoordinates1[0]
                            and abs(carPositions[carPos1][1]-carPositions[carPos2][1]) < distanceCoordinates1[0]
                            and carPos1 != carPos2):
                        print(f"{timestamp}s: Car {carPos1} bumped into car {carPos2}!\n{carPositions}\n")

        line_count+=1
        
plt.show()
            