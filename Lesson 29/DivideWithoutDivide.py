def Divide(dividend, divisor):
    # sign = (-1 if ((dividend < 0) ^ (divisor < 0)) else 1)
    if ((dividend < 0) ^ (divisor < 0)):
        sign = -1
    else:
        sign = 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    tempNum = 0

    for i in range(31, -1, -1):
        if (tempNum + (divisor << i) <= dividend):
            tempNum = tempNum + (divisor << i)
            quotient = quotient | (1 << i)

    if sign == -1:
        quotient = -quotient
    
    return quotient

x = int(input("Enter X (dividend) for X / Y :  "))
y = int(input("Enter Y (divisor) for X / Y :  "))

func = Divide(x, y)
print(f"The result of {x} / {y} = {func}")
