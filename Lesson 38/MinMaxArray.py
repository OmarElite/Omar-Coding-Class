def MinimumElement(arr, arr_size):
    temp = arr[0]
    for i in range(1, arr_size):
        temp = min(temp, arr[i])

    return temp

def MaximunElement(arr, arr_size):
    temp = arr[0]
    for i in range(1, arr_size):
        temp = max(temp, arr[i])

    return temp

array1 = [12, 256, 45, 67, 1]
array_size = len(array1)

result_min = MinimumElement(array1, array_size)
result_max = MaximunElement(array1, array_size)
print(f"Maximum Element is {result_max} and Minimum Element is {result_min}")
