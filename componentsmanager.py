inventory = {
    "resistor": {"quantity": 50, "unit_price": 0.05, "unit": "ohms", "value": 470},
    "capacitor": {"quantity": 30, "unit_price": 0.10, "unit": "uF", "value": 100},
    "led": {"quantity": 100, "unit_price": 0.25, "unit": "mA", "value": 20},
    "transistor": {"quantity": 20, "unit_price": 0.75, "unit": "V", "value": 5},
    "inductor": {"quantity": 15, "unit_price": 0.30, "unit": "mH", "value": 10}
}

print("EE Component Manager")
print("--------------------")
print("1. View all components")
print("2. Search component")
print("3. Add component")
print("4. Total inventory value")
print("--------------------")

choice = int(input("Select option: "))

if choice == 1:
    for components, details in inventory.items():
        print(f"Component: {components} | Unit Price: {details['unit_price']} | Unit: {details['unit']} | Value: {details['value']}")

elif choice == 2:
    search_components = input("Enter component name: ").lower()
    if search_components in inventory:
        print(f"Component: {search_components}")
        print(f"Quantity: {inventory[search_components]['quantity']}")
        print(f"Unit Price: {inventory[search_components]['unit_price']}")
        print(f"Unit: {inventory[search_components]['unit']} ")
        print(f" Value: {inventory[search_components]['value']}")
    else:
        print("Components not found!")
elif choice == 3:
    component_name = input("Enter name of component: ")
    component_quantity = input("Enter component quantity: ")
    component_unit_price = input("Enter unit price of component: ")
    component_unit = input("Enter the SI unit of component: ")
    component_value = input("Enter the value of component: ")
    inventory[component_name] = {'quantity' : component_quantity, 'unit_price' : component_unit_price, 'unit' : component_unit, 'value' : component_value}
    print(f"{component_name} added successfully!")
elif choice == 4:
    total_inventory_value = 0
    for components, details in inventory.items():
            total_inventory_value += details['quantity'] * details['unit_price']
    print(f"Total Inventory Value: ${total_inventory_value}")