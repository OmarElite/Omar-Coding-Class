def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1, 4, 3, 2, 6]
missing_number = find_missing_number(arr)
print("Missing number:", missing_number)
