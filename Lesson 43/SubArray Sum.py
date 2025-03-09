def SubArraySum(arr, arr_size, s):
    for i in range(arr_size):
        current_sum = arr[i]

        # Sum of Sub Array Starting with i
        j = i + 1
        while j <= arr_size:
            if current_sum == s:
                print(f"Sum found between index {i} and {j-1}")

                return 1

            if current_sum > s or j == arr_size:
                break

            current_sum = current_sum + arr[j]
            j = j + 1

    print("No Sub Array found")
    return 0

ArraySize = int(input("Enter the Array Size :  "))
Array = []
for i in range(ArraySize):
    get_array_elements = int(input("Enter The Elements of the Array :  "))
    Array.append(get_array_elements)

find_sum = 10
SubArraySum(Array, ArraySize, find_sum)
