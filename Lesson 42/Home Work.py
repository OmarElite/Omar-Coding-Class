def longest_alternating_subarray(arr):
    max_length = 1
    curr_length = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 1

    return max_length

a = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]
print("Output:", longest_alternating_subarray(a))
