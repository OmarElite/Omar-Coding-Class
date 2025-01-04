def TotalSetBit(number):
    count = 0

    while number:
        if number & 1 == 1:
            count = count + 1

        number = number >> 1

    return count

num = int(input("Enter any Number to check how many SetBits are in :  "))
result = TotalSetBit(num)
print()
print(f"Total SetBit is {result}")
