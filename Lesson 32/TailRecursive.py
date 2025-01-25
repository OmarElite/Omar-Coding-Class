def TailRecursive(n, num):
    if n > num:
        return

    print(n)

    TailRecursive(n+1, num)


number = int(input("Enter a number to display 1 intill the number itself :  "))
TailRecursive(1, number)
