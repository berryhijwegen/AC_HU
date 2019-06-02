import csv, functions, matplotlib.pyplot as plt, numpy as np, re, copy

# Read data into variable data and note columns with non-floats in it.
with open('resources/utrecht.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    headers = {}
    data = {}
    nonNumericIndexes = []
    for row in csv_reader:
        if(line_count == 0):
            for i in range(len(row)):
                headers[row[i]] = i
                data[i] = []
        
        else:
            if 'JJ00' not in row[headers['Perioden']]:
                i = 0
                for element in row:
                    try:
                        float(element)
                        data[i].append(float(element))
                    except:
                        data[i].append(element)
                        if i not in nonNumericIndexes:
                            nonNumericIndexes.append(i)
                    i+=1
        line_count+=1

# List all columns with their index, let user choose 1.
while(True):
    for header in headers:
        if headers[header] not in nonNumericIndexes and headers[header] is not 0:
            print(f"{headers[header]}: {header}")

    userInput = input("Choose a index: ")

    index = int(userInput)

    # Get key by value
    if index in headers.values() and index not in nonNumericIndexes and index is not 0:
        index = int(userInput)
        for key, value in headers.items():
            if value == index:
                header = key

        # Sort and show all data, functions in external file 'functions.py'
        dataset = copy.copy(data[index])
        print(dataset)
        sortedData = functions.sort(data[index])
        print(header)
        print(f"Average:            \n{functions.average(dataset)}")
        _modus = functions.modus(dataset)
        print(f"Modus:              \n{_modus[0]}: {_modus[1]} time(s)")
        print(f"Median:             \n{functions.median(sortedData)}")
        print(f"Standard deviaton:  \n{functions.standardDeviation(dataset)}")

        # Show histogram with confindence interval
        fig, ax = plt.subplots()

        binwidth = (max(dataset) - min(dataset)) / 40
        
        plt.hist(dataset, bins=np.arange(min(dataset), max(dataset) + binwidth, binwidth))
        
        avg = functions.average(dataset)
        plt.axvline(x=avg, color='red')

        for value in functions.confidenceInterval(dataset):
            plt.axvline(x=value, color='green', linestyle=':')

        plt.ylabel('Count')
        plt.xlabel('Value')
        plt.title(re.sub(r"(\w)([A-Z])", r"\1 \2", header).split('_')[0])
        plt.show()

        # Show graph with all data and trend line
        x, y, b = functions.linearRegression(dataset)
        fig, ax = plt.subplots()
        # plot points
        plt.scatter(x, y, color = "m",marker = "o", s = 10) 

        # predicted response vector 
        y_pred = [b[0] + (e * b[1]) for e in x]
    
        # plot regression line
        plt.plot(x, y_pred, color = "g")

        plt.xlabel('Periode') 
        plt.ylabel(re.sub(r"(\w)([A-Z])", r"\1 \2", header).split('_')[0]) 
        plt.xticks(np.arange(min(x), max(x)+1, 1.0))
        ax.set_xticklabels(data[headers['Perioden']])
        every_nth = 36
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        plt.title('Trend line')
        plt.show()

        break
    else:
        print('This index is not listed. Choose another.')