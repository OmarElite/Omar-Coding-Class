# Calculate Time Complaxity of Recursive Function
def TimeComplexity(number):
    if number <= 0:
        return
    
    print("Calculating ...")

    if number >= 2:
        print(number/2)
        TimeComplexity(number/2)
        print()

TimeComplexity(8)