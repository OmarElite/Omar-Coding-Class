def FindWater(arr, arr_size):
    left_bar = [0] * arr_size # Array to hold the height of left tallest bar
    right_bar = [0] * arr_size
    
    water = 0

    # fill left array
    left_bar[0] = arr[0]
    for i in range(1, arr_size):
        left_bar[i] = max(left_bar[i-1], arr[i])

    # fill right array 
    right_bar[arr_size-1] = arr[arr_size-1]
    for i in range(arr_size-2, -1, -1):
        right_bar[i] = max(right_bar[i+1], arr[i])
    
    # Water trapped for any bar chould be max of the left and min of the right
    for i in range(arr_size):
        water = water + min(left_bar[i], right_bar[i]) - arr[i]
    
    return water

myArray = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ArraySize = len(myArray)

result = FindWater(myArray, ArraySize)
print(f"The amount of water trapped : {result}")
