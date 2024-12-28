from math import sqrt

number = int(input("Enter a Number to be check :  "))

if number > 1:
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            print(f"{number} is not a Prime Number")
            break
    else:
        print(f"{number} is a Prime Number")

else:
    print(f"{number} is not a Prime Number")
    