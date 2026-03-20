first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
department = input("Which department? ")
level = input("What level are you in currently? ")
print(f'-------------')
print(f'-------------')
print(f'Name: {first_name} {last_name}')
print(f'Department: {department}')
print(f'Level: {level}')
print(f'-------------')
print(f'-------------')
#Scholarship/ Loan Screening System
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your gpa: "))
monthly_income = float(input("What is your monthly income? "))
credit_score = input("Do you have a good credit score? (yes/no) ")
criminal_record = input("Do you have a criminal record? (yes/no) ")

if len(name) < 3:
    print("Error!")
elif len(name) > 50:
    print("Error!")
else:
    if gpa >= 3.5 and age <= 25:
        print(f"Congratulations {name} you qualify for the scholarship.")
    else:
        print("You do not qualify")

#Loan Eligibility
if (monthly_income > 2000 or credit_score.lower() == 'yes') and criminal_record.lower()=='no':
    print("Congratulations, you qualify for a loan")

#Payment Simulation
tuition = 10000
balance = tuition
monthly_payment = float(input("How much would you want to pay monthly? "))
while balance > 0:
    balance -= monthly_payment
    print(f"Balance: {balance}")
    if balance <= 0:
        print("Tuition fully paid")

