sensor_readings = [] #Container to store entered values

num_readings = int(input('Enter the number of readings to log: '))

for i in range(num_readings):
    temp = float(input(f'Enter reading {i+1}: '))
    sensor_readings.append(temp)

Total = 0
for n_r in sensor_readings:
     Total+=n_r
Maximum_Reading = max(sensor_readings)
Minimum_Reading = min(sensor_readings)
average = Total/len(sensor_readings)

high_values = []
for r in sensor_readings:
     if r > 30:
          high_values.append(r)
print("\n---Data Logger Report---")
print(f'Readings: {sensor_readings}')
print(f'Maximum Reading: {Maximum_Reading}')
print(f'Minimum Reading: {Minimum_Reading}')
print(f'Average: {average}')
print("Values above 30°C:")
for i in range(len(sensor_readings)):
    if sensor_readings[i] > 30:
        print(f"Reading {i+1} -> {sensor_readings[i]}")