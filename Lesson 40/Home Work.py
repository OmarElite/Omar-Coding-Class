def max_difference(arr):
    if not arr or len(arr) < 2:
        return 0  # No valid difference

    min_val = arr[0]
    max_diff = 0

    for num in arr:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)

    return max_diff

# Example usage:
a = [4, 5, 234, 2, 6, 82, 234, 5234]
print("Output:", max_difference(a))
