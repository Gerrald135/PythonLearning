names = []
scores = []

number_of_student = int(input("How many students are there? "))

for i in range(number_of_student):
    name = input("Enter student's name: ")
    score = int(input("Enter student's score: "))
    if score <= 50:
        print("Student failed!")
    else:
        print("Student passed!")

    names.append(name)
    scores.append(score)

for n, s in zip(names, scores):
    print(f"Name: {n}, Score: {s}")

#Summary
total_score = 0
for k in scores:
    total_score+=k
average = total_score/len(scores)
maximum = max(scores)
minimum = min(scores)

# Find the student who got those scores
top_student = names[scores.index(maximum)]
lowest_student = names[scores.index(minimum)]
#index allows you to access to the location of a data
print(f"\nAverage score: {average}")
print(f"Highest score: {maximum} by {top_student}")
print(f"Lowest score: {minimum} by {lowest_student}")

print(f"Average score: {average}")
print(f"Highest score: {maximum}")
print(f"Lowest score: {minimum}")