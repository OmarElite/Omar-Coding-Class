
number = int(input("Enter a number to check :  "))

# Checking if the number is greater then 50 or not

if number > 50: #Outer if to check the first condition
    print("The number is Greater than 50")
    if number % 2 == 0:  #Inner If to check the second condition
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is less than or equals 50")
