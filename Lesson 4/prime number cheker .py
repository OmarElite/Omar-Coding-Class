number = int(input("Enter any number to be checked : "))

flag = False #bool

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break

if flag:
    print(f"{number} is not a Prime number")
else:
    print(f"{number} is a Prime number ")
