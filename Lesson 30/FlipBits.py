def Flips(fn, sn):
    flip = 0

    while fn > 0 or sn > 0:
        temp1 = fn & 1
        temp2 = sn & 1

        if temp1 != temp2:
            flip = flip + 1
        
        fn = fn >> 1
        sn = sn >> 1

    return flip

first_num = int(input("Enter the first number :  "))
second_num = int(input("Enter the second number :  "))

result = Flips(first_num, second_num)
print(f"Number of Flips needed = {result}")
