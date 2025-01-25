def HeadRecursive(n, num):
    if n > num:
        return
    
    HeadRecursive(n+1, num)

    print(n)


number = int(input("Enter Number to print number down to 1 : "))
HeadRecursive(1, number)
