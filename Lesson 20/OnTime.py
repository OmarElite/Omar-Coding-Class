def OnTime(number):
    iteration = 0
    for i in range(1, number+1):
        iteration = iteration+1
    
    print(f"Where number is {number}, the iteration = {iteration}")
    print()

OnTime(56)
OnTime(2)
OnTime(7891)
print()

print("With every 'number' the time taken iteration will linearly")