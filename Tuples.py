#Tuples
#Tuples are immutable. i.e, they can't be modified
#We can only get information about tuples
#tuples are placed in brackets()
#Tuples are used when the items are not to be changed within the code. eg numerical constants, etc
'''
numbers = (1, 2, 3)
print(numbers) '''

'''
reading = ('12:00', 5.0, 0.02)

reading[1] = 6.0
time, v, i = reading '''

#Unpacking
'''
results = (100, 0.25)

r_val, p_rating = results
print(f"The resistor is {r_val} ohms with a {p_rating} W rating") '''

'''
physics_consts = (299792458, '1.602e-19')
physics_consts.append(1)
print(physics_consts) '''

#When the tuple contains a single value, include a comma at the end to ensure the editor identifies it as a tuple otherwise it would be identified as just a number in a parenthesis
'''
const = (9,)
print(const) '''

'''
poles = [(0, 0), (10, 5), (20, 10)]

for x, y in poles:
    print(f"Pole at X: {x}, Y: {y}") '''

bands = (800, 900, 1800, 2100)
high_bands = bands[2:]

print(high_bands) #When tuples are sliced, they maintain their original data types. 