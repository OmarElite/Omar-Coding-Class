def Rotate(arr, arr_size):
    temp = arr[0]
    for i in range(arr_size-1):
        arr[i] = arr[i+1]
    
    arr[arr_size-1] = temp

def Rotation(arr, arr_size, n):
    for i in range(n):
        Rotate(arr, arr_size)

def DisplayArray(arr, arr_size):
    for i in range(arr_size):
        print(arr[i], end=" ")
    
myArray = [12, 12, 31, 85, 2, 3, 63, 576]
n = 4 # Group for rotation
array_size = len(myArray)

DisplayArray(myArray, array_size)
print()
print("Array after rotaion : ")
Rotation(myArray, array_size, n)
DisplayArray(myArray, array_size)
