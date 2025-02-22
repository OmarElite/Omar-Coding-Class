def Reverse(arr, arr_size, n): # n is the Group Size for reverse
    temp = 0
    
    while temp < arr_size:
        start = temp
        end = min(temp + n-1, arr_size-1) # When array size can not be divide by the n

        while start < end: # Reverse the sub-array [start, end]
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1
        
        temp = temp + n
    
array1 = [5, 23, 5, 23, 1, 23, 5, 136, 7, 56]
n = 4  # The Group size of reversing
array_size = len(array1)

Reverse(array1, array_size, n)

for i in range(array_size):
    print(array1[i], end = " ")
