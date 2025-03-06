def MaxSubArraySum(arr, arr_size):
    max = -9999
    curr_max = 0

    # Add current element to the curr_max and check if curr_max > max, than update max value
    for i in range(arr_size):
        curr_max = curr_max + arr[i]
        if curr_max > max:
            max = curr_max

        if curr_max < 0:
            curr_max = 0
    
    return max

Array = []
Array_Size = int(input("Enter the Array Size :  "))

for i in range(Array_Size):
    ask_user = int(input("Enter the Array elements :  "))
    Array.append(ask_user)

result = MaxSubArraySum(Array, Array_Size)
print(f"The maximum Sub Array Sum is {result}")
