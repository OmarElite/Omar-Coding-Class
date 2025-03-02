# Find the maximum consecutive 1s in an array of 1 and 0
def MaximumLenght(arr, arr_size):
    counter = 0
    max1 = 0

    # Code for array of 1 and 0
    """for i in range(arr_size):
        if arr[i] == 0: # If we find 0 then reset the counter
            counter = 0
        else:
            counter = counter + 1
            max1 = max(max1, counter)"""
    
    # Code for array of 1 and Other numbers
    for i in range(arr_size):
        if arr[i] != 1:
            counter = 0
        else:
            counter = counter + 1
            max1 = max(max1, counter)
    
    return max1

MyArray = [1, 1, 8, 50, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 1, 1]
ArraySize = len(MyArray)

result = MaximumLenght(MyArray, ArraySize)
print(f"The Maximum consecutive 1s is : {result}")
