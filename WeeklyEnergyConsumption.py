houses = ["House A", "House B", "House C"]

energy_data = [
    [12, 15, 14, 10, 9, 11, 13],   # House A (Mon–Sun)
    [20, 22, 19, 18, 21, 23, 24],  # House B
    [8, 7, 9, 6, 5, 7, 8]          # House C
]

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


for house, energy_used in zip(houses, energy_data):
    for day, energy in zip(days, energy_used):
        status = 'High'

        if energy > 20:
                status = 'High'
        else:
                status = 'ok'
        print(f"{house} - {day}: {energy} kWh [{status}]")

total= [0]*len(energy_data)
for i, energy_used in enumerate(energy_data):
        total[i] += sum(energy_used)

for house, totals, in zip(houses, total):
     print(f"{house} total consumption per week: {totals} ")

for house, energy_used in zip(houses, energy_data):
          Highest_energy = max(energy_used)
          day_index = energy_used.index(Highest_energy)
          highest_day = days[day_index]
          print(f"{house} highest usage: {Highest_energy} on {highest_day}")
