
def BMI(weight, height):
    return weight / (height * height)


wnh = float(input("Enter the weight in kg : "))
hng = float(input("Enter the height in metres : "))

result = BMI(wnh, hng)
print(f"The BMI is {result}")
