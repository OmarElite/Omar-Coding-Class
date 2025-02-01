def CheckPowerOf4(number):
    if number <= 0:
        return False
    
    if number == 1:
        return True
    
    if number % 4 == 0:
        return CheckPowerOf4(number // 4)
    
    return False

num = int(input("Enter your number :  "))
result = CheckPowerOf4(num)
if result:
    print(f"Yes, The number {num} is a power of 4")
else:
    print(f"No, The number {num} is not a power of 4")
