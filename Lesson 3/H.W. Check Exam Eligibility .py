"""import datetime

current_year = datetime.datetime.now().year

birth_year = int(input("Enter your birth year :  "))

age = current_year - birth_year

exam_year = int(input("Enter the exam year :  "))
print()

if age >= 18 and current_year < exam_year:
    print("You are eligible to take the exam.")
else:
    if age < 18:
        print("You are not eligible because you are under 18.")
print()
"""

ad = int(input("Enter total number of your attendance days : "))
na = int(input("Enter number of absent days :  "))

percentage = (ad - na ) / ad * 100

print(f" You attendance is {percentage}")

if (percentage < 75):
    print("You are not eligible for the exam")
else:
    print("You are eligible for the exam")