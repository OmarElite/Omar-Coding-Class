def min_flips(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            if arr[i] == 0:
                print(f"From {i} to ", end="")
            else:
                print(i-1)
    
    if arr[-1] == 0:
        print(n-1)

arr = [0, 1, 1, 0, 0, 0, 1, 1]
min_flips(arr)

# To visualize final array after conversion
print("arr =", [0]*len(arr))
