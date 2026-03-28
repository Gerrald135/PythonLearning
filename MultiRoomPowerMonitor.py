room_info = [
    ('room A', '01'), ('room B', '02'), ('room C', '03')
]

sensor_readings = [(200, 45, 230), (23, 34, 200), (45, 12, 350)]

sensor_types = ["Voltage(V)", "Current(A)", "Power Consumption(W)"]

faults = []
for (room_name, room_id), reading in zip(room_info, sensor_readings):
    for type, value in zip(sensor_types, reading):
        status = 'Ok'

        if type == "Voltage" and value > 240:
            print('Overvoltage!')
        elif type == "Current" and value > 30:
            print('Excessive Curent!')
        elif type == "Power" and value > 500:
            print('Overpower!')
        if status != 'Ok':
            faults.append((room_name, room_id, type, value, status))

        print(f"{room_name} ({room_id}): {type} -> {value}")

# Initialize sums
sums = [0] * len(sensor_types)

for readings in sensor_readings:
    for i, value in enumerate(readings):
        sums[i] += value

# Compute averages
averages = [s / len(sensor_readings) for s in sums]

print("\n---AVERAGE SENSOR VALUES---")
for sensor, avg in zip(sensor_types, averages):
    print(f"{sensor}: {avg:.2f}")

print("\n---FAULT SUMMARY---")
if faults:
    for f in faults:
        print(f"Room: {f[0]} ({f[1]}), Sensor: {f[2]}, Value: {f[3]}, Fault: {f[4]}")
else:
    print("No faults detected.")