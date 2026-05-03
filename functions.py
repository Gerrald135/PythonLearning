#functions allows us to write reusable codes or logic into a single logic. It starts with the def(define) keyword to show it's a function being defined. The return keyword sends a value back to the caller and also terminates the function.
'''def greet(name):
    print(f"Hello {name}")

greet("Jerry")

def add(a, b):
    return a+b

result = add(2, 3)
print(result) '''

'''
#Ohms Law
def ohms_law(voltage, resistance):
    current = voltage/resistance
    return current

results = ohms_law(12, 100)
print(f"Current: {results} A") '''

'''
#2
def circuit_analysis(voltage, resistance):
    current = voltage/resistance
    power = (voltage**2/resistance)
    return current, power #return value1, value2 allows to unpack and return more than a single value.
current, power = circuit_analysis(2, 10)
print(f"Current: {current}A")
print(f"Power: {power}W")''' 

'''
def greet(name = 'stranger'): #default parameters allows us to have fallback value if the user doesn't provide one.
    print(f"Hello {name}")

greet()

def resistor_divider(r1, r2, vin = 5):
    vout = vin*r2/(r1+r2)
    return vout
result = resistor_divider(1000, 2200)
result1 = resistor_divider(1000, 2200, vin = 12)
print(f"Vout (5V supply): {result:.2f}")
print(f"Vout(12V supply): {result1:.2f}") '''

'''
#3
def get_current(voltage, resistance):
    current = voltage/resistance
    return current
def get_power(voltage, current):
    power = voltage * current
    return power
def full_analysis(voltage, resistance):
    current = get_current(voltage, resistance)
    power = get_power(voltage, current)
    return voltage, resistance, current, power
v, r, c, p = full_analysis(12, 100)
print("--------------")
print(f"Voltage: {v}")
print(f"Resistance: {r}")
print(f"Current: {c}")
print(f"Power: {p}") '''

'''
#4
def rc_time_constant(resistance, capacitance):
    tau = resistance * capacitance
    return tau
def charge_time(resistance, capacitance, cycles = 5):
    tau = rc_time_constant(resistance, capacitance)
    time = cycles * tau
    return time, tau
time, tau = charge_time(resistance = 1000, capacitance = 0.000470)
time1, tau1 = charge_time(resistance= 1000, capacitance = 0.000470, cycles = 3)
print(f"Charge time: {time*1000:.2f}ms")
print(f"Charge time: {time1*1000:.2f}ms")
print(f"Time Constant: {tau*1000:.2f}ms")
print(f"Time Constant: {tau1*1000:.2f}ms") '''

'''
#Functions with dictionaries
#5
def component_summary(name, details):
    print(f"Quantity: {details['quantity']}")
    print(f"Unit price: {details['unit_price']}")
    print(f"Unit: {details['unit']}")
    print(f"value {details['value']}")
inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05, "unit": "ohms", "value": 470},
    "capacitor": {"quantity": 30, "unit_price": 0.10, "unit": "uF", "value": 100},
    "led": {"quantity": 100, "unit_price": 0.25, "unit": "mA", "value": 20},
}

def inventory_report(inventory):
    for name, details in inventory.items():
        print(f"----------{name}--------")
        component_summary(name, details)
    return inventory
inventory_report(inventory) '''

'''
#6
def equipment_summary(names, details):
    print(f"Brand: {details['brand']}")
    print(f"Price: {details['price']}")
    print(f"Status: {details['status']}")
lab = {
    "oscilloscope": {"brand": "Rigol", "price": 450, "status": "available"},
    "multimeter": {"brand": "Fluke", "price": 120, "status": "available"},
    "power_supply": {"brand": "Keysight", "price": 300, "status": "in repair"}
}


def lab_report(lab):
    for names, details in lab.items():
        print(f"---{names}---")
        equipment_summary(names, details)
    return lab
lab_report(lab) '''

'''
def component_check(names, details):
    print(f"Value: {details['value']}")
    print(f"Unit: {details['unit']}")
    print(f"Quantity: {details['quantity']}")
    if details['quantity'] > 0:
            print('In stock')
    else:
            print('Out of stock')

components = {
    "capacitor": {"value": 100, "unit": "uF", "quantity": 30},
    "resistor": {"value": 470, "unit": "ohms", "quantity": 0},
    "led": {"value": 20, "unit": "mA", "quantity": 15}
}

def pcb_report(components):
    for names, details in components.items():
        print(f"---{names}---")
        component_check(names, details)
    return components
pcb_report(components) '''

#Functions with lists
'''
def print_items(items):
    for item in items:
        print(item)

resistors = [470, 1000, 2200]
print_items(resistors)
'''
'''
resistances = [470, 1000, 2200, 330, 680]

def average_resistance(resistances):
    total = sum(resistances)
    average = total/len(resistances)
    return average
result = average_resistance(resistances)
print(f"Average Resistance: {result:.2f}") '''
'''
#3

resistances = [470, 1000, 2200, 330, 680, 4700, 100]

def filter_resistors(resistances, threshold):
    filtered = []
    for resistance in resistances:
        if resistance > threshold:
            filtered.append(resistance)
    return filtered
result = filter_resistors(resistances, 500)
print(f"Resistors above 500 ohms: {result}") '''

#4
'''
resistors = [470, 1000, 2200]
def series_resistance(resistors):
        Rtotal = sum(resistors)
        return Rtotal

def parallel_resistance(resistors):
    total = 0
    for resistor in resistors:
        total += 1/resistor
    Rtotal = 1/total
    return Rtotal
results = series_resistance(resistors)
result = parallel_resistance(resistors)
print(f"Series: {results:.2f}")
print(f"Parallel: {result:.2f}") '''

'''
#5
resistor_pairs = [(1000, 2200), (470, 1000), (3300, 3300)]
def voltage_divider_array(resistor_pairs, vin):
    vouts = []
    for r1, r2 in resistor_pairs:
        Vout = vin*r2/(r1+r2)
        vouts.append(Vout)
    return vouts
result = voltage_divider_array(resistor_pairs, vin = 12)
for i, vout in enumerate(result):
    print(f"Vout {i+1}: {vout:.2f} V") '''

#6
'''
components = ["resistor", "capacitor", "resistor", "led", "resistor", "capacitor", "transistor", "led", "led"]

def count_components(components):
    component_count = {}
    for component in components:
        if component in component_count:
            component_count[component] += 1
        else:
            component_count[component] = 1
    return component_count
result = count_components(components)
for component, count in result.items():
    print(f"{component}: {count}") '''
'''
#7
readings = [3.3, 5.0, 1.8, 2.5, 4.7, 3.3, 0.9, 5.0, 2.1]
def analyze_signals(readings):
    highest_voltage = max(readings)
    lowest_voltage = min(readings)
    average = sum(readings)/len(readings)
    number_of_readings = len(readings)
    return highest_voltage, lowest_voltage, average, number_of_readings
h, l, a, n = analyze_signals(readings)
print(f"Highest Voltage: {h}V")
print(f"Lowest Voltage: {l}V")
print(f"Average: {a:.2f}V")
print(f"Count: {n} readings") '''

'''
#8
signals = [(1, 4), (2, 4), (3, 4), (1, 2), (0.5, 1)]
def pwm_analysis(signals):
    dutyCycle = []
    for on_time, period in signals:
        dutycycle = (on_time/period)*100
        dutyCycle.append(dutycycle)
    return dutyCycle
result = pwm_analysis(signals)
for i, duty in enumerate(result):
    print(f"Signal {i+1}: {duty}%") '''

'''
#9
configs = [
    {"r_feedback": 10000, "r_input": 1000},
    {"r_feedback": 47000, "r_input": 4700},
    {"r_feedback": 100000, "r_input": 10000},
]
def opamp_gain(configs):
    gains = []
    for details in configs:
        gain = -(details['r_feedback']/details['r_input'])
        gains.append(gain)
    return gains
result = opamp_gain(configs)
for i, Gain in enumerate(result):
    print(f"Config {i+1}: {Gain}") '''

#10
'''
logs = [
    {"sensor": "temperature", "voltage": 2.3, "timestamp": 1},
    {"sensor": "pressure", "voltage": 4.1, "timestamp": 2},
    {"sensor": "temperature", "voltage": 1.8, "timestamp": 3},
    {"sensor": "pressure", "voltage": 3.7, "timestamp": 4},
    {"sensor": "temperature", "voltage": 4.9, "timestamp": 5},
]

def log_summary(logs):
    total = 0
    total_readings = len(logs)
    highest = logs[0]
    lowest = logs[0]
    summary = {}
    for reading in logs:
        total += reading['voltage']
        if reading['voltage'] > highest['voltage']:
            highest = reading
        if reading['voltage'] < lowest['voltage']:
            lowest = reading
    
    average = total / total_readings
    
    summary = {
        "total_readings": total_readings,
        "average_voltage": average,
        "highest": highest,
        "lowest": lowest
    }
    return summary
results = log_summary(logs)
print(f"Total Readings: {results['total_readings']}")
print(f"Average Voltage: {results['average_voltage']:.2f} V")
print(f"Highest: {results['highest']['sensor']} at timestamp {results['highest']['timestamp']} → {results['highest']['voltage']}V")
print(f"Lowest: {results['lowest']['sensor']} at timestamp {results['lowest']['timestamp']} → {results['lowest']['voltage']}V") '''

#11
batteries = [
    {"battery_id": "A1", "voltage": 3.7, "temperature": 28},
    {"battery_id": "A2", "voltage": 3.2, "temperature": 45},
    {"battery_id": "A3", "voltage": 4.1, "temperature": 32},
    {"battery_id": "A4", "voltage": 2.9, "temperature": 38},
    {"battery_id": "A5", "voltage": 3.5, "temperature": 25},
]

def battery_report(batteries):
    total = 0
    total_batteries = len(batteries)
    hottest = batteries[0]
    weakest = batteries[0]
    summary = {}
    for battery in batteries:
        total += battery['voltage']
        if battery['temperature'] > hottest['temperature']:
            hottest = battery
        if battery['voltage'] < weakest['voltage']:
            weakest = battery
    average = total/total_batteries
    summary = {'total_batteries' : total_batteries,
               'hottest' : hottest,
               'weakest' : weakest, 
               'average' : average
               }
    return summary
Summary = battery_report(batteries)
print(f"Total Batteries: {Summary['total_batteries']}")
print(f"Average Voltage: {Summary['average']:.2f}V")
print(f"Hottest Battery: {Summary['hottest']['battery_id']} at {Summary['hottest']['temperature']} deg C")
print(f"Weakest Battery: {Summary['weakest']['battery_id']} at {Summary['weakest']['voltage']}V")
