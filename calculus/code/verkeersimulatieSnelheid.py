import csv
import matplotlib.pyplot as plt
import numpy as np

timestamps      = []
speedDataCar1   = []
speedDataCar2   = []

times, positionsCar1, positionsCar2 = np.loadtxt('resources/verkeerssimulatie-rechteweg-posities.csv', unpack=True, delimiter=';')
previous_row = None
maxSpeedCar1 = minSpeedCar1 = maxSpeedCar2 = minSpeedCar2 = 0
for i in range(len(times)):
    timestamp           = float(times[i])
    posCar1             = float(positionsCar1[i])
    posCar2             = float(positionsCar2[i])
    
    prevTimestamp       = float(times[i - 1]) if i != 0 else timestamp
    prevPosCar1         = float(positionsCar1[i- 1]) if i != 0 else posCar1
    prevPosCar2         = float(positionsCar2[i- 1]) if i != 0 else posCar2
    
    elapsedTime         = round(timestamp - prevTimestamp,1)
    traveledDistance1   = posCar1 - prevPosCar1
    traveledDistance2   = posCar2 - prevPosCar2
    
    currSpeedCar1KM     = traveledDistance1 / elapsedTime if elapsedTime != 0 else 0
    currSpeedCar2KM     = traveledDistance2 / elapsedTime if elapsedTime != 0 else 0

    
    speedDataCar1.append(currSpeedCar1KM * 36)
    speedDataCar2.append(currSpeedCar2KM * 36)
    timestamps.append(timestamp)

    maxSpeedCar1 = currSpeedCar1KM if currSpeedCar1KM > maxSpeedCar1 or i == 0 else maxSpeedCar1
    minSpeedCar1 = currSpeedCar1KM if currSpeedCar1KM < minSpeedCar1 or i == 0 else minSpeedCar1

    maxSpeedCar2 = currSpeedCar2KM if currSpeedCar2KM > maxSpeedCar2 or i == 0 else maxSpeedCar2
    minSpeedCar2 = currSpeedCar2KM if currSpeedCar2KM < minSpeedCar2 or i == 0 else minSpeedCar2

print(f'minSpeed car 1: {minSpeedCar1 * 36} km/h')
print(f'minSpeed car 1: {minSpeedCar2 * 36} km/h')
print(f'maxSpeed car 2: {maxSpeedCar1 * 36} km/h')
print(f'maxSpeed car 2: {maxSpeedCar2 * 36} km/h')


plt.plot(timestamps, speedDataCar1)
plt.plot(timestamps, speedDataCar2)
plt.xlabel('Time in seconds')
plt.ylabel('Speed in km/h')
plt.show()