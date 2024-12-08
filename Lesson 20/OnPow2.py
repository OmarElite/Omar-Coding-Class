def OnSquareTime(number):
    iteration = 0
    for i in range(0, number): # This is for Row
        for j in range(0, number): # This is for Column
            print("*", end="")
            iteration = iteration+1
        print()

    print(f"Where number is {number}, the iteration = {iteration}")
    print()

OnSquareTime(5)
OnSquareTime(10)
OnSquareTime(2)
print()

print("With every 'number', the time taken is number^2")
print("O(n^2)")