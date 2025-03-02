def MoveAllZeros(arr, arr_size):
    nonZero = 0
    zero = 0   # Zero will hold the position of the nonZero number

    while nonZero != arr_size:
        if arr[nonZero] != 0:
            arr[nonZero], arr[zero] = arr[zero], arr[nonZero]
            zero = zero + 1
        
        nonZero = nonZero + 1

Array1 = []
ArraySize = int(input("Enter the Array Size :  "))

for i in range(ArraySize):
    elemnts = int(input("Enter the array element (Make sure some of them contening 0 number) :  "))
    Array1.append(elemnts)

print()
print(f"Original array = {Array1}")

MoveAllZeros(Array1, ArraySize)
print()
print(f"Updated Array after moving all of the 0 at the end of the array :")
print(Array1)
print()
