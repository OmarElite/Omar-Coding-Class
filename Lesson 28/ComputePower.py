def ComputePower(x, y):
    result = 1

    while y > 0:
        if y % 2 == 0:
            x = x * x
            y = y >> 1
        else:
            result = result * x
            y = y - 1
    
    return result

fnum = int(input("Enter X for X ^ Y :  "))
snum = int(input("Enter Y for X ^ Y :  "))

func = ComputePower(fnum, snum)
print(f"The total is {func}")
