def Powerof2(number):
    if number <= 0:
        return False
    
    result = number & (number-1)
    if result == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number tobe check :  "))

result = Powerof2(num)
if result:
    print(f"The number {num} is a power of 2")
else:
    print(f"The number {num} is not a power of 2")
    