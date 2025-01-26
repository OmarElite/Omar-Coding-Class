def LargestElemnt(a):
    Length = len(a)
    if Length == 1:
        return a[0]
    
    return max(a[0], LargestElemnt(a[1:]))

MyList = [52, 65, 6, 678, 23]
result = LargestElemnt(MyList)
print(f"The most Big element of the Array is : {result}")
