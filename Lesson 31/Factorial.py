def Factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * Factorial(number - 1)
    
num = int(input("Enter any Number :  "))
result = Factorial(num)

print(f"Factorial of {num} is : {result}")
