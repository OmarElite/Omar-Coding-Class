def EquilibriumPoint(arr):
    left_side_sum = 0
    right_side_sum = 0

    arr_size = len(arr)
    for i in range(arr_size):
        left_side_sum = 0
        right_side_sum = 0

        # Get left Sum
        for j in range(i):
            left_side_sum = left_side_sum + arr[j]
        
        # Get right Sum
        for j in range(i+1, arr_size):
            right_side_sum = right_side_sum + arr[j]

        # If left sum and Right Sum value are the same than we already find the Equilibrium Point
        if left_side_sum == right_side_sum:
            return i
    
    return -1

Array = [-4, 6, 2, 0, 0, 1, 1]

result = EquilibriumPoint(Array)
print(f"The Equilibrium Point is on the index : {result}")
