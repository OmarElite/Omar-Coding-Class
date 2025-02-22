def Leader(arr, arr_size):
    current_max = arr[arr_size-1] # Usualy the right most is the Leader
    print(current_max)

    for i in range(arr_size-2, -1, -1):
        if current_max < arr[i]:
            print(arr[i])
            current_max = arr[i]

myArray = [245, 16, 17, 4, 3, 5]
array_size = len(myArray)
Leader(myArray, array_size)

