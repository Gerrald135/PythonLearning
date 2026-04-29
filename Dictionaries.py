#Dictionaries are used when we want to store informations that come as key value pairs
'''customer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verified" : True
}

#We can access elements wwithin the dictionaries using []. When the key doesnt' exist, we get a keyerror
customer["name"]
print(customer['name'])

#We can equally use the get method to access a key. Using the get method means the compiler doesn't give an error info. It just specify the key isn't present
print(customer.get("name"))

#We can also supply values to the keys
print(customer.get("birthday", "1988"))

#Adding new values to keypairs
customer["birthday"] = "Jan 1 1980"
print(customer["birthday"])

#Exercise
phone = input("Phone: ")

Phone  = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
}

output = ""
for ch in phone:
    output += Phone.get(ch, "!") + " "
print(output)
'''
'''
#Resistance calc
color_code = input("Band 1: ")
color_code2 = input("Band 2: ")

colors = {
    "Black" : 0,
    "Brown" : 1,
    "Red" : 2,
    "Orange" : 3,
    "Yellow" : 4,
    "Green" : 5,
    "Blue" : 6,
    "Violet" : 7,
    "Grey" : 8,
    "White" : 9
}

band1 = colors.get(color_code.capitalize(), "Invalid color")
band2 = colors.get(color_code2.capitalize(), "Invalid color")

if band1 == "Invalid color" or band2 == "Invalid color":
    print("Invalid Color!")
else:
    resistance = (band1*10 + band2)
print(resistance) '''
'''
#Resistance Calc w/ 3 bands
color_code = input("Band 1: ")
color_code1 = input("Band 2: ")
color_code2 = input("Band 3: ")

colors = {
    "Black" : 0,
    "Brown" : 1,
    "Red" : 2,
    "Orange" : 3,
    "Yellow" : 4,
    "Green" : 5,
    "Blue" : 6,
    "Violet" : 7,
    "Grey" : 8,
    "White" : 9
}

multiplier = {
    "Black" :  1,       # 10^0
    "Brown":  10,      # 10^1
    "Red":    100,     # 10^2
    "Orange": 1000,    # 10^3
    "Yellow": 10000,   # 10^4
    "Green":  100000,  # 10^5
}

band1 = colors.get(color_code.capitalize(), "Invalid Color")
band2 = colors.get(color_code1.capitalize(), "Invalid Color")
band3 = multiplier.get(color_code2.capitalize(), "Invalid Color")

if band1 == "Invalid Color" or band2 == "Invalid Color" or band3 == "Invalid Color":
    print("Invalid Color!")

else:
    resistance = (band1*10 + band2) * band3
    if resistance >= 1000000:
        print(f"Resistance: {resistance/1000000} M-ohms")
    elif resistance >= 1000:
        print(f"Resistance: {resistance/1000} k-ohms")
    else:
        print(f"Resistance: {resistance} ohms")
'''
'''
#Ohm's law calc
components = {
    "voltage" : "none",
    "current" : "none",
    "resistance" : "none"
}

print("Components")
print("----------")
print("1. Current")
print("2. Voltage")       
print("3.Resistance")
print("----------")

component = int(input("Select component 1 (1, 2 or 3): "))
component1 = int(input("Select component 2 (1, 2 or 3): "))
if component == 1 and component1 == 2:
    components["current"] = float(input("Enter value of current: "))
    components["voltage"] = float(input("Enter value of voltage: "))
    components["resistance"] = components["voltage"]/components["current"]
    print(f"{components['resistance']} ohm")
elif component == 1 and component1 == 3:
    components["current"] = float(input("Enter value of current: "))
    components["resistance"] = float(input("Enter value of resistance: "))
    components["voltage"] = components["current"]*components["resistance"]
    print(f"{components['voltage']} V")
elif component == 2 and component1 == 3:
    components["voltage"] = float(input("Enter value of voltage: "))
    components["resistance"] = float(input("Enter value of resistance: "))
    components["current"] = components["voltage"]/components["resistance"]
    print(f"{components['current']} A") '''

'''
#Inventory
inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05},
    "capacitor": {"quantity": 30, "unit_price": 0.10},
    "led": {"quantity": 100, "unit_price": 0.25}
}

Component = input("Enter component name: ").lower()
if Component in inventory:
    total_price = float(inventory[Component]["quantity"] * (inventory[Component]["unit_price"]))
    print(f"Quantity: {inventory[Component]['quantity']}")
    print(f"Unit Price: $ {inventory[Component]["unit_price"]}")
    print(f"Total: $ {total_price}")
else:
    print("Component not available") '''

'''
#InventorySummary
inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05},
    "capacitor": {"quantity": 30, "unit_price": 0.10},
    "led": {"quantity": 100, "unit_price": 0.25}
}
total_price = 0
#the items funcion in python is to make the compiler see both the key and value. Else it treats the keys as separate and tries to do sequentuential unpacking, iterating over each. 
for component, details in inventory.items():
    print(f"{component} | {details['quantity']} | ${details['unit_price']}")
    total_price += details['quantity'] * details['unit_price']

print(f"Total Price: {total_price}") '''

'''
#Voltage divider
circuit = {
    "Vin": 12,
    "R1": 1000,
    "R2": 2200
}

circuit["Vout"] = float(circuit["Vin"] * circuit["R2"] / (circuit["R1"] + circuit["R2"]))

circuit["I"] = float(circuit["Vin"]/(circuit["R1"] + circuit["R2"]))

for key, value in circuit.items():
   print(f"{key}: {value}") '''

lab = {
    "oscilloscope": {"brand": "Rigol", "price": 450},
    "multimeter": {"brand": "Fluke", "price": 120},
    "power_supply": {"brand": "Keysight", "price": 300}
}

for components, details in lab.items():
    for components, details in lab.items():
        print(f"{components} - Brand: {details['brand']} | Price: ${details['price']}")