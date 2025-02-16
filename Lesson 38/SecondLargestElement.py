def DisplaySecondLargestElement(arr, arr_size):
    largest = second_largest = -2147
    for i in range(arr_size):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    return second_largest

array1 = [1, 2, 3,4, 5, 6, 7, 8, 9]
array_size = len(array1)

result = DisplaySecondLargestElement(array1, array_size)
print(f"The second Largest element = {result}")
