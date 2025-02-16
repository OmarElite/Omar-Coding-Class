def DisplayMean(arr,arr_size):
    total_sum = 0
    for i in range(arr_size):
        total_sum = total_sum + arr[i]

    mean_array = total_sum / arr_size
    return mean_array

def DisplayMedian(arr, arr_size):
    # Sort the Array
    sorted(arr)

    if arr_size % 2 != 0:  # Array Size is odd number
        median_array = arr[int(arr_size/2)]
    else:
        median_array = (arr[int((arr_size-1)/2)]+ arr[int(arr_size/2)])/2

    return median_array

array1 = [1, 4, 5, 2, 5, 8, 5, 2, 6, 8]
array_size = len(array1)

result_mean = DisplayMean(array1, array_size)
result_median = DisplayMedian(array1, array_size)
print(f"Mean = {result_mean} / Median = {result_median}")
