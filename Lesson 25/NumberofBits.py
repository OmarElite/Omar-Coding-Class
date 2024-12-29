
def NumberOfBits(number):
    count = 0

    while number:
        count = count + 1
        number = number >> 1

    return count

num = int(input("Enter any number to be check :  "))
result = NumberOfBits(num)

print(f"Number of Bits of {num} is {result}")
