# Substation info (static metadata)
substation_info = [
    ("North-Grid", 'T01'),
    ("Central-Hub", 'T102'),
    ("South-Station", 'C103')
]

# Sensor readings (dynamic, changes over time)
sensor_data = [
    [230, 12, 35],   # North-Grid: Voltage, Current, Temperature
    [245, 15, 55],   # Central-Hub
    [210, 10, -5]    # South-Station
]

# Sensor types
sensor_types = ["Voltage", "Current", "Temperature"]

# Thresholds for fault detection
VOLTAGE_MAX = 240
TEMP_MAX = 50
TEMP_MIN = 0

# Container for detected faults
faults = []

# Monitor each substation
for (name, line_id), readings in zip(substation_info, sensor_data):
    for sensor, value in zip(sensor_types, readings):
        status = "OK"

        # Check for faults
        if sensor == "Voltage" and value > VOLTAGE_MAX:
            status = "OVERVOLTAGE"
        elif sensor == "Temperature" and value > TEMP_MAX:
            status = "OVERHEAT"
        elif sensor == "Temperature" and value < TEMP_MIN:
            status = "FAILURE"

        # Store faults
        if status != "OK":
            faults.append((name, line_id, sensor, value, status))

        # Print sensor reading with status
        print(f"{name} ({line_id}) -> {sensor}: {value} [{status}]")

# Summary of faults
print("\n---FAULT SUMMARY---")
if faults:
    for f in faults:
        print(f"Substation: {f[0]} ({f[1]}), Sensor: {f[2]}, Value: {f[3]}, Fault: {f[4]}")
else:
    print("No faults detected.")