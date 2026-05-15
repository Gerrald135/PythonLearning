'''f = open("data.txt", "w")
#the open function is used to open the file, the "data.txt" is the filename, w, r, a are the modes which means write, read and append to a file respectively. f is a placeholder for the file ansd can be used to call certain functions on it.
#writing to a file
f = open("data.txt", "w")
f.write("hello")
f.close()
#reading from a file
f = open("data.txt", "r")
content = f.read()
f.close()
print(content)
#a much cleaner way is using the with. this automatically closes the file when done
with open("data.txt", 'w') as f:
    f.write("helo")
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

#1
resistances = [470, 1000, 2200, 330, 680]
with open("resistances.txt", "w") as f:
    for resistance in resistances:
        f.write(str(resistance) + "\n")
with open("resistances.txt", "r") as f:
    contents = f.read()
    print(contents) '''

#2
'''resistances = [470, 1000, 2200, 330, 680]
with open("resistances.txt", "w") as f:
    for resistance in resistances:
        f.write(str(resistance) + "\n")
new_value = input("Enter new resistance value: ")
with open("resistances.txt", "a") as f:
    f.write(new_value + "\n")
with open("resistances.txt", "r") as f:
    content = f.read()
    print(content) '''

#4
'''components = {
    "resistor": 470,
    "capacitor": 100,
    "inductor": 10
}
with open("components.txt", "w") as f:
    for component in components:
        f.write(str(component) + ", " + str(components[component]) + '\n')
loaded_components = {}
with open("components.txt", "r") as f:
    for line in f: #iterates through the keys and values in the dictionary
        line = line.strip() #removes the newline, \n
        parts = line.split(",") #breaks the string into lists
        name = parts[0].strip()
        value = int(parts[1])
        loaded_components[name] = value
print(loaded_components) '''

'''
#5
inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05},
    "capacitor": {"quantity": 30, "unit_price": 0.10},
    "led": {"quantity": 100, "unit_price": 0.25}
}
with open("inventory.txt", "w") as f:
    for component, details in inventory.items():
        f.write(str(component) + " , " + str(details['quantity']) + " , " + str(details['unit_price']) + "\n")
loaded_inventory = {}
with open("inventory.txt", "r") as f:
    for line in f:
        line = line.strip()
        parts = line.split(" , ")
        name = parts[0]
        quantity = int(parts[1])
        unit_price = float(parts[2])
        loaded_inventory[name] = {"quantity" : quantity, "unit_price" : unit_price}
print(loaded_inventory) '''

#6
'''
inventories = {
    "resistor": {"quantity": 50, "unit_price": 0.05, "unit": "ohms", "value": 470},
    "capacitor": {"quantity": 30, "unit_price": 0.10, "unit": "uF", "value": 100},
    "led": {"quantity": 100, "unit_price": 0.25, "unit": "mA", "value": 20},
    "transistor": {"quantity": 20, "unit_price": 0.75, "unit": "V", "value": 5},
    "inductor": {"quantity": 15, "unit_price": 0.30, "unit": "mH", "value": 10}
}
with open("inventories.txt", "w") as f:
    for components, details in inventories.items():
        f.write(str(components) + " , " + str(details['quantity']) + " , " + str(details["unit_price"]) + " , " + str(details["unit"]) + " , " + str(details['value']) + "\n")
print("EE Component Manager")
print("--------------------")
print("1. View all components")
print("2. Search component")
print("3. Add component")
print("4. Total inventory value")
print("--------------------")
choice = int(input("Enter your choice: "))
if choice == 1:
    loaded_inventories = {}
    with open("inventories.txt", "r") as f:
        for component in f:
            component = component.strip()
            parts = component.split(' , ')
            name = parts[0]
            quantity = int(parts[1])
            unit_price = float(parts[2])
            unit = parts[3]
            value = int(parts[4])
            loaded_inventories[name] = {'quantity' : quantity, 'unit_price' : unit_price, 'unit' : unit, 'value' : value}
    print(loaded_inventories)
elif choice == 2:
    search_components = input("Enter component name: ").lower()
    if search_components in inventories:
        print(f"Component: {search_components}")
        print(f"Quantity: {inventories[search_components]['quantity']}")
        print(f"Unit Price: {inventories[search_components]['unit_price']}")
        print(f"Unit: {inventories[search_components]['unit']} ")
        print(f" Value: {inventories[search_components]['value']}")
    else:
        print("Components not found!")
elif choice == 3:
        component_name = input("Enter name of component: ")
        component_quantity = input("Enter component quantity: ")
        component_unit_price = input("Enter unit price of component: ")
        component_unit = input("Enter the SI unit of component: ")
        component_value = input("Enter the value of component: ")
        with open("inventories.txt", "a") as f:
            f.write(component_name + " , " + component_quantity + " , " + component_unit_price + " , " + component_unit + " , " + component_value)
        with open("inventories.txt", "r") as f:
            content = f.read()
            print(content) '''

#Error Handling
#try/except helps us to handle filenotfound errors without the program crashing
'''try:
    with open("inventory.txt", 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found!") '''

'''
try:
    with open("inventori.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("No inventori file found. Starting with empty inventori.")
    inventori = {} '''

#JSON(javascript object notation)
#It is used for storing and exchanging structured data. It looks almost identical to a dictionary.
''' import json

# Writing
data = {"resistor": {"quantity": 50, "unit_price": 0.05}}
with open("data.json", "w") as f:
    json.dump(data, f)#writes data to file

# Reading
with open("data.json", "r") as f:
    data = json.load(f)#reads file back into dictionary
print(data) '''

'''
import json
inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05},
    "capacitor": {"quantity": 30, "unit_price": 0.10},
    "led": {"quantity": 100, "unit_price": 0.25}
}
with open("inventory.json", "w") as f:
    json.dump(inventory, f)

with open("inventory.json", "r") as f:
    inventory = json.load(f)
print(inventory) '''
'''
import json
Inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05, "unit": "ohms", "value": 470},
    "capacitor": {"quantity": 30, "unit_price": 0.10, "unit": "uF", "value": 100},
    "led": {"quantity": 100, "unit_price": 0.25, "unit": "mA", "value": 20}
}

def save_inventory(Inventory):
    with open("Inventory.json", 'w') as f:
        json.dump(Inventory, f)

def load_inventory():
    try:
        with open("Inventory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found!")
        return {}

def add_component(Inventory):
        name = input("Enter component name: ")
        quantity = int(input("Enter component quantity: "))
        unit_price = float(input("Enter unit price: "))
        unit = input("Enter unit of component: ")
        value = input("Enter component value: ")
        Inventory[name] = {'quantity' : quantity, 'unit_price' : unit_price, 'unit' : unit, 'value' : value}
        save_inventory(Inventory)
        print(f"{name} added succesfully!")

save_inventory(Inventory)
Inventory = load_inventory()
add_component(Inventory)
print(Inventory)
'''
import json
logs = [
    {"sensor": "temperature", "voltage": 2.3, "timestamp": 1},
    {"sensor": "pressure", "voltage": 4.1, "timestamp": 2}
]

def save_logs(logs):
    with open("logs.json", 'w') as f:
        json.dump(logs, f)

def load_logs():
    try:
        with open("logs.json", "r") as f:
           return json.load(f)
    except FileNotFoundError:
        print("File not found!")
        return []

def add_log(logs):
    sensor = input("Enter sensor name: ")
    voltage = float(input("Enter voltage reading: "))
    timestamp = len(logs) + 1
    logs.append(
        {
            'sensor' : sensor,
            'voltage' : voltage,
            'timestamp' : timestamp
        }
    )
    save_logs(logs)

def view_logs(logs):
    for log in logs:
        print(f"Timestamp {log['timestamp']} | Name: {log['sensor']} | Voltage: {log['voltage']}")

save_logs(logs)
logs = load_logs()
add_log(logs)
view_logs(logs)