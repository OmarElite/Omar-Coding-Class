def Kadane(arr):
    arr_size = len(arr)
    max_so_far = 0
    max_ending_here = 0

    for i in range(arr_size):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    
    return max_so_far

def MaximumCircularSum(a):
    arr_size = len(a)

    # Apply Kadane Algorithm if no Circular is Needed
    max_kadane = Kadane(a)

    # Find sum of all elements and invert them
    max_wrap = 0

    for i in range(arr_size):
        max_wrap = max_wrap + a[i]
        a[i] = -a[i]
    
    # Apply Kadane Algorithm to find minimum Inverted SubArray
    max_wrap = max_wrap + Kadane(a)

    # The maximum Circular sum while be a Maximum of 2 sum
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
    
Array = []
Array_Size = int(input("Enter the Array Size :  "))

for i in range(Array_Size):
    ask_user = int(input("Enter the Array Elements : "))
    Array.append(ask_user)

print(Array)
result = MaximumCircularSum(Array)
print(f"The maximum Crcular sum is : {result}")
