
# Converting Answers from str to float :
height = float(input("Enter your height in cm = "))
weight = float(input("Enter your weight in kg = "))

BMI = weight / ((height / 100) * (height / 100))

print(f"BMI is {BMI}")

if BMI <= 18.5:
    print("You are under weight")
elif 18.5 < BMI <= 24.9:
    print("You are heilthy :)")
elif 24.9 < BMI <= 29.9:
    print("You are over weight")
elif 29.9 < BMI <= 34.9:
    print("You are severely over weight !")
elif 34.9 < BMI <= 39.9:
    print("You are obese !!")
else:
    print("You are severely obese !!!")
