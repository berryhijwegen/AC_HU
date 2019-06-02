# Bubble sort algorithm, replace if bigger
def sort(lst):
    for iter_num in range(len(lst)-1,0,-1):
        for i in range(iter_num):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst

def length(lst):
    l = 0
    for item in lst:
        l += 1
    return l

def total(lst):
    _sum = 0
    for item in lst:
        _sum += item
    return _sum

def average(lst):
    return total(lst) / length(lst)

# Count and return highest
def modus(lst):
    hits = {}
    highest = []
    for value in lst:
        if value in hits:
            hits[value] += 1
        else:
            hits[value] = 1
        
        highest = [value, hits[value]] if  highest == [] or hits[value] > highest[1] else highest
    return highest

# return middle or average or 2 middle values, depends if even or odd
def median(lst):
    l = length(lst)
    if l % 2 == 0:
        total = (lst[int((l) / 2 - 0.5)]) + (lst[int((l) / 2 + 0.5)])
        return total / 2
    elif l % 2 == 1:
        return lst[int((l)/2)]


def standardDeviation(lst):
    avg = average(lst)
    quadrants = []
    for element in lst:
        quadrants.append((element - avg)**2)
    return average(quadrants)**.5

def confidenceInterval(lst):
    # Calculate 95% confidence interval
    std = standardDeviation(lst)
    l = length(lst)
    avg = average(lst)
    return [avg + 1.96 * (std / (l**.5)), avg - 1.96 * (std / (l**.5))]


def linearRegression(lst):
    x = list(range(1, length(lst) + 1))
    y = lst

    n = length(x)
    avg_x, avg_y = average(x), average(y) 
  
    # Calculating cross-deviation and deviation about x
    SS_xy = total([a*b for a,b in zip(y,x)]) - n*avg_y*avg_x
    SS_xx = total([a*b for a,b in zip(x,x)]) - n*avg_x*avg_x 

    # Calculating regression coefficients 
    b_1 = SS_xy / SS_xx
    b_0 = avg_y - b_1*avg_x 
  
    return x, y, (b_0, b_1)