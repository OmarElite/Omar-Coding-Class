# making recursive function
def Factorial(n):
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)
    

number = int(input("Enter a Number to Get the Factorial = "))

# Check if the number is less than or equal 0

if number < 0:
    print("Sorry there is no Factorial for negative number")
elif number == 0:
    print("The Factorial of 0 is 1")
else:
    result = Factorial(number)
    print(f"The Factorial of {number} is {result}")
