import csv

def getDirections(csvFile):
    directions = {}
    carNums = None
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if(line_count == 1):
                for i in range(len(row)):
                    directions[int(carNums[i])] = row[i]
            carNums = row
            line_count+=1

    return directions