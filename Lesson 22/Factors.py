def DisplayFactors(number):
    print(f"The Factors of {number} are ")

    for i in range(1, number+1):
        if number % i == 0:
            print(i)

num = int(input("Enter your number to find it factor = "))
DisplayFactors(num)
