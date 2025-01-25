def IncreaseDecrease(n, num):
    if n < 1 or n > num:
        return
    
    print(n)
    print()
    
    # Applying Head Recursive to Display Increasing Number
    IncreaseDecrease(n-1, num)
    print()

    print(n)

number = int(input("Enter any Number : "))
IncreaseDecrease(number , number)
