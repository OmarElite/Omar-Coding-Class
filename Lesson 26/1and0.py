def NumberOfBits(number):
    ones = 0
    zeros = 0

    while number:
        if number & 1 == 1:
            ones = ones + 1
        else:
            zeros = zeros+1

        number = number >> 1

    print(f"Number of 1 in the Binary Code of {number} is :  {ones}")
    print(f"Number of 0 in the Binary Code of {number} is :  {zeros}")

num = int(input("Enter a number to be check the amount of the Bits :  "))
NumberOfBits(num)
