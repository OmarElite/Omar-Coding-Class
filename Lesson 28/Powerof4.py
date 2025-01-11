def Powerof4(number):
    count = 0

    # Checking whether there is only 1 SetBit exist
    if (number & (~(number & (number - 1)))):
        while number > 1: # Count 0 Bits before setbits
            number = number >> 1
            count = count + 1
        
        # If count is Even number the result while be True
        if count % 2 == 0:
            return True
        else:
            return False

num = int(input(" Enter any number to be check :  "))
fun = Powerof4(num)

if fun:
    print(f"{num} is a power of 4")
else:
    print(f"{num} is not a power of 4")
    