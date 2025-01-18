import math

def PrintPowerSet(array1, array_size):
    # Find Total element possible in the power set
    PowerSetSize = (int) (math.pow(2, array_size))
    Outer = 0
    Inner = 0
    
    for Outer in range(0, PowerSetSize):
        for Inner in range(0, array_size):
            if ((Outer & (1 << Inner)) > 0):
                print(array1[Inner], end=" ")
        
        print()

size = int(input("Enter Array Size :  "))
Set = []

for i in range(size):
    number = int(input("Enter the elements of the Array :  "))
    Set.append(number)

print()
print("The possible combination of array elements are :  ")
PrintPowerSet(Set, size)
