
def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    return x / y

first_number = int(input("Please enter first number =  "))
second_number = int(input("Please enter second number = "))

# Calling function : Addition
add = Addition(first_number, second_number)
print(f"{first_number} + {second_number} = {add}")
print()

sub = Subtraction(first_number, second_number)
print(f"{first_number} - {second_number} = {sub}")
print()

mult = Multiplication(first_number, second_number)
print(f"{first_number} x {second_number} = {mult}")
print()

div = Division(first_number, second_number)
print(f"{first_number} / {second_number} = {div}")
print()
