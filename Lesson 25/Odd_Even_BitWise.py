
def OddOrEven(number):
    if number ^ 1 == number+1:
        return True
    else:
        return False
    
num = int(input("Enter your number to be check :  "))

result = OddOrEven(num)
if result == True:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")
