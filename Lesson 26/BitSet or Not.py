def SetBitOrNot(number, position):
    mask = 1

    if (position & mask) == 1 or (position & mask) == 0:
        if number & (1 << (position - 1)):
            print(f"Bit on the position {position} is SetBit")
        else:
            print(f"Bit on the position {position} is not SetBit")

num = int(input("Enter any number :  "))
pos = int(input("Enter the Bit position to be check :  "))

SetBitOrNot(num, pos)
