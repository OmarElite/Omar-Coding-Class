row = int(input("Enter the number of rows :  "))

# Nested Loops (Loops inside of other loops)
for i in range(row): # Outer loops representing rows
    for j in range(0, i+1): # Inner loops representings coloms
        print("*", end=" ")

    print()

