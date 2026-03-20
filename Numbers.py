numbers = []
abs_values = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num > 0:
        print("The number is positive!")
    elif num < 0:
        print("The number is negative!")
    else:
        print("It is zero!")

    numbers.append(num)
    abs_values.append(abs(num))

for n, a in zip(numbers, abs_values):
    print(f"Number: {n}, Absolute value: {a}")

print("Sum and Average of numbers")
total_numbers = 0
for k in numbers:
    total_numbers += k
average = total_numbers/len(numbers)
print(f"Sum: {total_numbers}")
print(f"Average: {average}")

print('Sum and average of absolute values')
total_absolutes = 0
for j in abs_values:
    total_absolutes += j
average = total_absolutes/len(abs_values)
print(f"Sum: {total_absolutes}")
print(f"Average: {average}")