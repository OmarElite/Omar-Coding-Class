def CheckSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    
    return a[0] <= a[1] and CheckSorted(a[1:])

MyList = [6, 8, 56, 123]

result = CheckSorted(MyList)
if result:
    print("Yes, the array is already sorted")
else:
    print("No, the array is not sorted")
